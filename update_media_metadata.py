"""
update_media_metadata.py

Uses the WordPress REST API to update media attachment fields in bulk.
For every image that already has alt text:
  - Title       → short (~7 words), first clause of alt text
  - Caption     → hashtag keywords from alt text  e.g.  #karnak #temple #egypt
  - Description → full alt text

Only updates fields that are empty or have auto-generated / generic values.

Requirements:
    pip install playwright && playwright install webkit
    Safari → Develop → Allow Remote Automation

Usage:
    WP_USER=admin WP_PASS=secret python update_media_metadata.py
"""

import asyncio
import os
import re
import sys
import pathlib
import getpass

SESSION_DIR = pathlib.Path(__file__).parent / ".wp_session"

try:
    from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
except ImportError:
    print("Playwright not found.  Run:  pip install playwright && playwright install webkit")
    sys.exit(1)

WP_URL   = "https://accessegypttravel.com"
API_MEDIA = f"{WP_URL}/wp-json/wp/v2/media"

# ── Generic / auto-generated value detection ──────────────────────────────────

GENERIC_RE = re.compile(
    r"^(IMG|DSC|DSCN|DCIM|DSC0|MVI|MOV|VID|PANO|BURST|PHOTO|PIC)[-_]?\d"
    r"|^\d{5,}$"
    r"|^[a-f0-9]{8}-[a-f0-9]{4}"
    r"|^(untitled|screenshot|image[-_]\d|photo[-_]\d|file[-_]\d)",
    re.IGNORECASE,
)

def needs_update(value: str) -> bool:
    v = (value or "").strip()
    if not v:
        return True
    return bool(GENERIC_RE.match(v))


# ── Field generators ──────────────────────────────────────────────────────────

def make_title(alt_text: str, max_words: int = 7) -> str:
    """First clause of alt text, capped at max_words."""
    text = alt_text.rstrip(".").strip()
    first_clause = text.split(",")[0].strip()
    words = first_clause.split()
    return " ".join(words[:max_words]) if len(words) > max_words else first_clause


_STOP = {
    "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "into", "as", "is", "are", "was", "were",
    "be", "been", "its", "their", "this", "that", "these", "those",
    "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "one", "large", "small", "covered", "standing", "seated", "posing",
    "wearing", "showing", "view", "seen", "taken", "front", "back", "row",
    "line", "set", "against", "near", "above", "below", "inside", "outside",
    "group", "several", "many", "multiple", "various", "colorful", "detailed",
    "ancient", "egyptian", "massive", "towering", "ornate", "carved", "painted",
}

_TRAVEL_TERMS = {
    "karnak", "luxor", "cairo", "aswan", "giza", "egypt", "nile", "sinai",
    "alexandria", "philae", "edfu", "dendera", "abydos", "saqqara",
    "temple", "pyramid", "sphinx", "tomb", "obelisk", "pharaoh", "mummy",
    "sarcophagus", "hieroglyph", "relief", "papyrus", "felucca", "cruise",
    "valley", "kings", "hatshepsut", "ramesses", "tutankhamun", "horus",
    "isis", "osiris", "ankh", "bazaar", "mosque", "coptic",
}

def make_caption(alt_text: str, max_tags: int = 6) -> str:
    """Extract keywords and return as space-separated #hashtags."""
    if not alt_text:
        return ""
    text = alt_text.rstrip(".").strip()
    words = text.split()
    tags: list[str] = []
    seen: set[str] = set()

    # Proper nouns (capitalized mid-sentence)
    for i, word in enumerate(words):
        clean = re.sub(r"[^a-zA-Z]", "", word)
        lower = clean.lower()
        if i > 0 and clean and clean[0].isupper() and lower not in _STOP and len(lower) > 2:
            if lower not in seen:
                tags.append(lower)
                seen.add(lower)

    # Known Egypt/travel keywords
    for word in re.findall(r"\b[a-z]+\b", text.lower()):
        if word in _TRAVEL_TERMS and word not in seen:
            tags.append(word)
            seen.add(word)

    return " ".join(f"#{t}" for t in tags[:max_tags])


# ── REST API helpers (run inside the browser via page.evaluate) ───────────────

_FETCH_GET = """
async ([url, nonce]) => {
    const r = await fetch(url, {headers: {'X-WP-Nonce': nonce}});
    const data = await r.json();
    const total = parseInt(r.headers.get('X-WP-Total') || '0');
    const pages = parseInt(r.headers.get('X-WP-TotalPages') || '1');
    return {ok: r.ok, status: r.status, total, pages, data};
}
"""

_FETCH_POST = """
async ([url, payload, nonce]) => {
    const r = await fetch(url, {
        method:  'POST',
        headers: {'Content-Type': 'application/json', 'X-WP-Nonce': nonce},
        body:    JSON.stringify(payload),
    });
    return {ok: r.ok, status: r.status};
}
"""


async def get_nonce(page) -> str:
    """Read the WP REST API nonce injected on every admin page."""
    nonce = await page.evaluate("window.wpApiSettings?.nonce ?? ''")
    return nonce or ""


async def login(page, context, username, password, storage_file) -> bool:
    await page.goto(f"{WP_URL}/wp-login.php")
    await page.fill("#user_login", username)
    await page.fill("#user_pass", password)
    await page.click("#wp-submit")
    try:
        await page.wait_for_url("**/wp-admin/**", timeout=15_000)
    except PlaywrightTimeoutError:
        print("ERROR: Login failed — check credentials.")
        return False
    await context.storage_state(path=str(storage_file))
    print("Logged in. Session saved.\n")
    return True


async def main() -> None:
    username = os.environ.get("WP_USER") or input("WordPress username: ").strip()
    password = os.environ.get("WP_PASS") or getpass.getpass("WordPress password: ")

    stats = {
        "total":          0,
        "skipped_no_alt": 0,
        "nothing_to_do":  0,
        "updated":        0,
        "errors":         0,
    }

    async with async_playwright() as pw:
        try:
            browser = await pw.webkit.launch(headless=False, slow_mo=50)
        except Exception as e:
            print(f"Could not launch Safari/WebKit: {e}")
            sys.exit(1)

        SESSION_DIR.mkdir(exist_ok=True)
        storage_file = SESSION_DIR / "storage_state.json"
        context = await browser.new_context(
            storage_state=str(storage_file) if storage_file.exists() else None
        )
        page = await context.new_page()

        # ── Auth ───────────────────────────────────────────────────────────────
        if storage_file.exists():
            print("Found saved session …")
            await page.goto(f"{WP_URL}/wp-admin/")
            await page.wait_for_load_state("networkidle")
            if "wp-login" in page.url:
                print("Session expired — logging in …")
                storage_file.unlink()
                if not await login(page, context, username, password, storage_file):
                    await browser.close(); return
            else:
                print("Session valid.\n")
        else:
            if not await login(page, context, username, password, storage_file):
                await browser.close(); return

        # Stay on admin dashboard to keep nonce fresh
        await page.goto(f"{WP_URL}/wp-admin/")
        await page.wait_for_load_state("networkidle")
        nonce = await get_nonce(page)
        if not nonce:
            print("ERROR: Could not read REST API nonce from admin page.")
            await browser.close(); return
        print(f"REST API nonce obtained.\n")

        # ── Collect all image attachments via REST API (100 per page) ──────────
        print("Fetching all media attachments …")
        all_items: list[dict] = []
        api_pg = 1

        while True:
            url = (f"{API_MEDIA}?per_page=100&page={api_pg}"
                   f"&media_type=image&context=edit"
                   f"&_fields=id,alt_text,title,caption,description")
            res = await page.evaluate(_FETCH_GET, [url, nonce])
            if not res["ok"] or not res["data"]:
                break
            all_items.extend(res["data"])
            print(f"  Page {api_pg}: {len(res['data'])} items  "
                  f"(total: {res['total']}, pages: {res['pages']})")
            if api_pg >= res["pages"]:
                break
            api_pg += 1

        stats["total"] = len(all_items)
        print(f"\nTotal images: {stats['total']}\n")

        # ── Process each attachment ────────────────────────────────────────────
        for pos, item in enumerate(all_items, start=1):
            att_id = item["id"]

            # Unpack REST API field objects.
            # With context=edit the "raw" key is always present (may be "").
            # Never fall back to "rendered" — it can contain empty HTML like <p></p>
            # which would wrongly pass the needs_update() check.
            def raw(field) -> str:
                if isinstance(field, dict):
                    r = field.get("raw")
                    if r is not None:
                        return r.strip()
                    # no raw key → strip HTML from rendered as last resort
                    rendered = re.sub(r"<[^>]+>", "", field.get("rendered") or "")
                    return rendered.strip()
                return (field or "").strip()

            alt   = raw(item.get("alt_text",    ""))
            title = raw(item.get("title",       ""))
            cap   = raw(item.get("caption",     ""))
            desc  = raw(item.get("description", ""))

            print(f"[{pos}/{stats['total']}]  id={att_id}", end="  ")

            if not alt:
                print("no alt text — skip")
                stats["skipped_no_alt"] += 1
                continue

            # Decide what to update
            updates: dict[str, str] = {}
            if needs_update(title):
                updates["title"]       = make_title(alt)
            if needs_update(cap):
                new_cap = make_caption(alt)
                if new_cap:                          # skip if no keywords extracted
                    updates["caption"] = new_cap
            if needs_update(desc):
                updates["description"] = alt

            if not updates:
                print("all fields OK")
                stats["nothing_to_do"] += 1
                continue

            print(f"updating {', '.join(updates.keys())}")
            for field, value in updates.items():
                print(f"     {field:<12}: {value[:70]}")

            # Wrap string values in {raw:} format as required by WP REST API
            api_payload = {k: {"raw": v} for k, v in updates.items()}

            # POST to REST API
            res = await page.evaluate(
                _FETCH_POST,
                [f"{API_MEDIA}/{att_id}", api_payload, nonce],
            )

            if res["ok"]:
                print("     → saved ✓")
                stats["updated"] += 1
            else:
                print(f"     → ERROR {res['status']}")
                # Refresh nonce on auth failure and retry once
                if res["status"] in (401, 403):
                    await page.goto(f"{WP_URL}/wp-admin/")
                    await page.wait_for_load_state("networkidle")
                    nonce = await get_nonce(page)
                    res2 = await page.evaluate(
                        _FETCH_POST,
                        [f"{API_MEDIA}/{att_id}", updates, nonce],
                    )
                    if res2["ok"]:
                        print("     → saved ✓ (after nonce refresh)")
                        stats["updated"] += 1
                    else:
                        print(f"     → still failing ({res2['status']}) — skipping")
                        stats["errors"] += 1
                else:
                    stats["errors"] += 1

        # ── Summary ────────────────────────────────────────────────────────────
        print("\n" + "═" * 54)
        print("FINISHED")
        print(f"  Total images              : {stats['total']}")
        print(f"  Skipped (no alt text)     : {stats['skipped_no_alt']}")
        print(f"  Nothing needed updating   : {stats['nothing_to_do']}")
        print(f"  Updated                   : {stats['updated']}")
        print(f"  Errors                    : {stats['errors']}")
        print("═" * 54)

        try:
            input("\nPress Enter to close …")
        except EOFError:
            pass
        await context.close()
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
