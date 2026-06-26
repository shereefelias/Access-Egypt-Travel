#!/usr/bin/env python3
"""
Batch photo processor for Access Egypt Travel.
Walks photos/originals/, generates website / social / thumbnail derivatives.
Applies watermark, strips sensitive metadata, embeds copyright.

NEVER modifies originals. All outputs use atomic writes.
Run:  python3 scripts/process_single_test.py [--dry-run] [--single <path>]
"""

import argparse
import hashlib
import math
import sys
from pathlib import Path

import piexif
from PIL import Image, ImageDraw, ImageFont, ImageOps

# ── Paths ─────────────────────────────────────────────────────────────────────
PHOTOS_ROOT = Path("/Users/shereefelias/Documents/Access Egypt Travel/photos")
ORIGINALS   = PHOTOS_ROOT / "originals"
WATERMARK   = PHOTOS_ROOT / "watermark" / "Access_Egypt_Travel_Logo.png"

SUPPORTED = {".jpg", ".jpeg", ".jfif", ".png", ".tif", ".tiff", ".webp"}

# ── Identity ──────────────────────────────────────────────────────────────────
ARTIST         = "John Gamil Gadalla"
COPYRIGHT      = "© 2026 Access Egypt Travel LLC. All rights reserved."
WEBSITE_URL    = "https://accessegypttravel.com"
CONTACT_EMAIL  = "info@accessegypttravel.com"
USAGE_TERMS    = (
    "No reproduction, redistribution, commercial use, or AI training "
    "without written permission from Access Egypt Travel LLC."
)

# ── Output specs ──────────────────────────────────────────────────────────────
OUTPUTS = {
    "website": {
        "dir":       PHOTOS_ROOT / "processed" / "website",
        "format":    "WEBP",
        "max_px":    1920,
        "quality":   82,
        "watermark": True,
        "metadata":  True,
        "ext":       ".webp",
    },
    "social": {
        "dir":       PHOTOS_ROOT / "processed" / "social",
        "format":    "JPEG",
        "max_px":    1440,
        "quality":   88,
        "watermark": True,
        "metadata":  True,
        "ext":       ".jpg",
    },
    "thumbnail": {
        "dir":       PHOTOS_ROOT / "processed" / "thumbnails",
        "format":    "WEBP",
        "max_px":    400,
        "quality":   75,
        "watermark": False,
        "metadata":  False,
        "ext":       ".webp",
    },
}

# ── Watermark settings ────────────────────────────────────────────────────────
WM_RELATIVE_WIDTH = 0.09   # 9% of output width
WM_OPACITY        = 0.65   # logo opacity 65%
WM_MARGIN         = 0.02   # 2% margin from edges
WM_MIN_WIDTH      = 600    # skip watermark if output narrower than this
WM_TEXT_OPACITY   = 0.12   # diagonal text — very light
WM_DIAGONAL_TEXT  = "Access Egypt Travel LLC"
WM_COPYRIGHT_TEXT = "© 2026 Access Egypt Travel LLC"


# ── Helpers ───────────────────────────────────────────────────────────────────

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def resize_fit(img: Image.Image, max_px: int) -> Image.Image:
    w, h = img.size
    longest = max(w, h)
    if longest <= max_px:
        return img.copy()
    scale = max_px / longest
    return img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)


def _load_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
    ]:
        try:
            return ImageFont.truetype(path, size)
        except (IOError, OSError):
            pass
    return ImageFont.load_default()


def _apply_diagonal_text(canvas: Image.Image) -> Image.Image:
    w, h = canvas.size
    font_size = max(20, int(w * 0.055))
    font = _load_font(font_size)
    angle = math.degrees(math.atan2(h, w))

    diag = int(math.sqrt(w * w + h * h))
    big = Image.new("RGBA", (diag, diag), (0, 0, 0, 0))
    big_draw = ImageDraw.Draw(big)
    bbox = big_draw.textbbox((0, 0), WM_DIAGONAL_TEXT, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx, ty = (diag - tw) // 2, (diag - th) // 2
    big_draw.text((tx, ty), WM_DIAGONAL_TEXT, font=font,
                  fill=(255, 255, 255, int(255 * WM_TEXT_OPACITY)))

    big_rotated = big.rotate(angle, resample=Image.BICUBIC, expand=False)
    left = (big_rotated.width - w) // 2
    top  = (big_rotated.height - h) // 2
    txt_layer = big_rotated.crop((left, top, left + w, top + h))
    return Image.alpha_composite(canvas, txt_layer)


def apply_watermark(img: Image.Image, wm_path: Path) -> Image.Image:
    if img.width < WM_MIN_WIDTH:
        return img

    out = img.convert("RGBA")
    out = _apply_diagonal_text(out)

    # Logo
    wm = Image.open(wm_path).convert("RGBA")
    target_wm_w = int(img.width * WM_RELATIVE_WIDTH)
    scale = target_wm_w / wm.width
    logo_h = max(1, int(wm.height * scale))
    wm = wm.resize((target_wm_w, logo_h), Image.LANCZOS)
    r, g, b, a = wm.split()
    a = a.point(lambda x: int(x * WM_OPACITY))
    wm = Image.merge("RGBA", (r, g, b, a))

    margin_x = int(img.width * WM_MARGIN)
    margin_y = int(img.height * WM_MARGIN)

    # Copyright text sized to logo width
    font_size = max(10, int(target_wm_w * 0.10))
    font = _load_font(font_size)
    tmp_draw = ImageDraw.Draw(out)
    bbox = tmp_draw.textbbox((0, 0), WM_COPYRIGHT_TEXT, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    text_gap = int(font_size * 0.3)

    block_h  = logo_h + text_gap + text_h
    block_top = img.height - block_h - margin_y
    logo_x   = img.width - target_wm_w - margin_x
    logo_y   = block_top
    text_x   = logo_x + (target_wm_w - text_w) // 2
    text_y   = block_top + logo_h + text_gap

    out.paste(wm, (logo_x, logo_y), mask=wm)

    txt_layer = Image.new("RGBA", out.size, (0, 0, 0, 0))
    txt_draw  = ImageDraw.Draw(txt_layer)
    txt_draw.text((text_x, text_y), WM_COPYRIGHT_TEXT, font=font,
                  fill=(255, 255, 255, int(255 * WM_OPACITY)))
    out = Image.alpha_composite(out, txt_layer)

    return out.convert("RGB")


def make_copyright_exif(raw_exif: bytes | None, capture_date: str | None,
                        description: str) -> bytes:
    STRIP_EXIF = {
        piexif.ExifIFD.BodySerialNumber,
        piexif.ExifIFD.LensSerialNumber,
        piexif.ExifIFD.MakerNote,
        piexif.ExifIFD.CameraOwnerName,
    }
    if raw_exif:
        try:
            exif = piexif.load(raw_exif)
        except Exception:
            exif = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}
    else:
        exif = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}

    exif["GPS"] = {}
    exif["thumbnail"] = None
    exif["1st"] = {}
    for tag in STRIP_EXIF:
        exif["Exif"].pop(tag, None)

    exif["0th"][piexif.ImageIFD.Artist]           = ARTIST.encode()
    exif["0th"][piexif.ImageIFD.Copyright]        = COPYRIGHT.encode()
    exif["0th"][piexif.ImageIFD.ImageDescription] = description.encode()
    exif["0th"][piexif.ImageIFD.Software]         = b"Access Egypt Travel Photo Pipeline"

    if capture_date:
        exif["Exif"][piexif.ExifIFD.DateTimeOriginal]  = capture_date.encode()
        exif["Exif"][piexif.ExifIFD.DateTimeDigitized] = capture_date.encode()

    comment = f"{USAGE_TERMS} | {WEBSITE_URL} | {CONTACT_EMAIL}"
    exif["Exif"][piexif.ExifIFD.UserComment] = b"UNICODE\x00" + comment.encode("utf-16-le")

    try:
        return piexif.dump(exif)
    except Exception:
        minimal = {
            "0th": {
                piexif.ImageIFD.Artist:    ARTIST.encode(),
                piexif.ImageIFD.Copyright: COPYRIGHT.encode(),
            },
            "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None,
        }
        return piexif.dump(minimal)


def get_capture_date(img: Image.Image) -> str | None:
    try:
        raw = img.info.get("exif")
        if not raw:
            return None
        exif = piexif.load(raw)
        dt = exif["Exif"].get(piexif.ExifIFD.DateTimeOriginal)
        if dt:
            return dt.decode("utf-8") if isinstance(dt, bytes) else dt
    except Exception:
        pass
    return None


def slug_from_path(path: Path) -> str:
    name = path.stem.lower().replace(" ", "-")
    return "".join(c if c.isalnum() or c == "-" else "-" for c in name).strip("-")


def output_filename(slug: str, short_hash: str, ext: str) -> str:
    return f"{slug}-{short_hash}{ext}"


def atomic_write(img: Image.Image, dest: Path, fmt: str, quality: int,
                 exif_bytes: bytes | None) -> None:
    partial = dest.with_suffix(dest.suffix + ".partial")
    dest.parent.mkdir(parents=True, exist_ok=True)

    save_kwargs: dict = {"format": fmt, "quality": quality}
    if fmt == "JPEG":
        save_kwargs["optimize"] = True
        save_kwargs["progressive"] = True
        if exif_bytes:
            save_kwargs["exif"] = exif_bytes
    elif fmt == "WEBP":
        save_kwargs["method"] = 6
        if exif_bytes:
            save_kwargs["exif"] = exif_bytes

    img.save(partial, **save_kwargs)
    Image.open(partial).verify()
    partial.rename(dest)


def process_one(source: Path, dry_run: bool) -> dict:
    """Process a single source image. Returns a result dict."""
    result = {"path": source, "status": "ok", "skipped": [], "error": None}

    try:
        # Safety: source must be inside originals
        assert source.is_relative_to(ORIGINALS)

        original_hash = sha256_file(source)
        short_hash    = original_hash[:10]
        rel_subdir    = source.parent.relative_to(ORIGINALS)
        slug          = slug_from_path(source)
        description   = " ".join(w.capitalize() for w in slug.replace("-", " ").split())

        img = Image.open(source)
        img = ImageOps.exif_transpose(img)
        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGB")

        raw_exif     = img.info.get("exif")
        capture_date = get_capture_date(img)

        for name, spec in OUTPUTS.items():
            dest = spec["dir"] / rel_subdir / output_filename(slug, short_hash, spec["ext"])

            if dest.exists() and not dry_run:
                result["skipped"].append(name)
                continue

            if dry_run:
                continue

            resized = resize_fit(img, spec["max_px"])
            work    = resized.convert("RGB") if resized.mode == "RGBA" else resized.copy()

            if spec["watermark"] and WATERMARK.exists():
                work = apply_watermark(work, WATERMARK)

            exif_bytes = make_copyright_exif(raw_exif, capture_date, description) \
                         if spec["metadata"] else None

            atomic_write(work, dest, spec["format"], spec["quality"], exif_bytes)

        # Verify original unchanged
        if sha256_file(source) != original_hash:
            result["status"] = "hash_changed"

    except Exception as e:
        result["status"] = "error"
        result["error"]  = str(e)

    return result


def collect_sources() -> list[Path]:
    sources = []
    for p in sorted(ORIGINALS.rglob("*")):
        if p.is_file() and p.suffix.lower() in SUPPORTED:
            sources.append(p)
    return sources


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Access Egypt Travel batch photo processor")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be processed, no writes")
    parser.add_argument("--single", type=str, help="Process one specific file instead of all")
    args = parser.parse_args()

    if args.single:
        sources = [Path(args.single)]
    else:
        sources = collect_sources()

    total = len(sources)
    print(f"\nAccess Egypt Travel — Batch Photo Processor")
    print(f"{'(DRY RUN) ' if args.dry_run else ''}Processing {total} image(s)\n")

    ok = skipped = errors = 0

    for i, source in enumerate(sources, 1):
        rel = source.relative_to(PHOTOS_ROOT)
        print(f"[{i:>3}/{total}] {rel}")

        result = process_one(source, dry_run=args.dry_run)

        if result["status"] == "error":
            print(f"        ERROR: {result['error']}")
            errors += 1
        elif result["status"] == "hash_changed":
            print(f"        WARNING: original hash changed after processing!")
            errors += 1
        else:
            if result["skipped"]:
                print(f"        skipped (already processed): {', '.join(result['skipped'])}")
                skipped += 1
            else:
                ok += 1

    print(f"\n{'─' * 50}")
    print(f"Done.  {ok} processed  |  {skipped} already existed  |  {errors} errors")
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
