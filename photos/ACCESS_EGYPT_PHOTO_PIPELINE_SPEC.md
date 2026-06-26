# Access Egypt Photo Pipeline

## Codex / CLI Build Specification

**Project owner:** Shereef Elias  
**Project:** Access Egypt Travel  
**Primary photo library path:**

```text
/Users/shereefelias/Documents/Access Egypt Travel/photos
```

This document is intended to be placed inside the project folder and used later as the master implementation prompt for Codex, Claude Code, Cursor, or another coding agent.

---

# 1. Project Goal

Build a production-quality local command-line application for processing, organizing, protecting, and cataloging a large personal travel-photo library.

The application should initially support at least 5,000 photos and remain practical for 100,000 or more records.

The system must prioritize:

1. Original-file safety
2. Copyright ownership and metadata
3. Repeatable bulk processing
4. Resume support after interruption
5. Duplicate detection
6. Website and social-media output generation
7. Private handling of GPS data
8. Local-first processing
9. Clear reporting and audit history
10. Future extensibility

The first version must not include a web dashboard, cloud upload, WordPress publishing, Meta publishing, or external AI processing.

---

# 2. Fixed Project Path

Use this as the default photo-library root:

```text
/Users/shereefelias/Documents/Access Egypt Travel/photos
```

All example commands, configuration defaults, and generated paths should use this root unless the user explicitly overrides it.

Because this path contains spaces, all shell commands must quote it.

Correct:

```bash
aep init --root "/Users/shereefelias/Documents/Access Egypt Travel/photos"
```

Incorrect:

```bash
aep init --root /Users/shereefelias/Documents/Access Egypt Travel/photos
```

---

# 3. Technology Stack

Use:

- Python 3.12 or newer
- Typer for the CLI
- Rich for terminal formatting and progress
- Pydantic for configuration validation
- SQLite for the main catalog
- Python `sqlite3` or SQLAlchemy 2.x
- Pillow for standard image processing
- ExifTool for EXIF, IPTC, and XMP metadata
- pytest for tests
- Ruff for linting and formatting
- mypy for type checking
- pathlib for filesystem paths
- hashlib for SHA-256 hashes

Optional dependencies:

- `rawpy` for RAW processing
- `pillow-heif` for HEIC support
- `ImageHash` for perceptual duplicate detection
- OpenCV for optional blur detection

Do not require Docker for normal use.

---

# 4. Core Safety Rules

The application must:

- Never overwrite originals
- Never rename originals automatically
- Never move originals automatically
- Never delete originals
- Never write metadata back to originals
- Never open originals in write mode
- Never use the originals directory as an output directory
- Resolve symbolic links before path-safety checks
- Reject output directories located inside the originals directory
- Record the original SHA-256 hash during scanning
- Recalculate and verify the source hash before processing
- Mark a source as changed if its hash no longer matches
- Create all derivatives from read-only source access
- Write outputs atomically using temporary files
- Never perform cloud uploads by default
- Never expose private GPS coordinates in normal CLI output

Original-file protection is more important than convenience.

---

# 5. Recommended Folder Structure

The application should use this structure:

```text
/Users/shereefelias/Documents/Access Egypt Travel/photos/
├── originals/
│   ├── 2025/
│   ├── 2026/
│   └── unsorted/
├── processed/
│   ├── website/
│   ├── social/
│   ├── social-4x5/
│   └── thumbnails/
├── rejected/
├── watermark/
│   └── access-egypt-watermark.png
├── database/
│   └── photos.db
├── reports/
├── logs/
├── backups/
├── config.json
└── README.md
```

The program may create missing folders except `originals`.

The application must not create, move, rename, or delete files inside `originals` unless a future command explicitly supports that behavior and requires confirmation.


## 5.1 Mirrored derivative folder structure

All processed outputs must preserve the exact relative folder structure found under `originals`.

Example source:

```text
/Users/shereefelias/Documents/Access Egypt Travel/photos/originals/cairo/pyramids/sunrise/IMG_1234.CR3
```

Required outputs:

```text
/Users/shereefelias/Documents/Access Egypt Travel/photos/processed/website/cairo/pyramids/sunrise/img-1234.webp

/Users/shereefelias/Documents/Access Egypt Travel/photos/processed/social/cairo/pyramids/sunrise/img-1234.jpg

/Users/shereefelias/Documents/Access Egypt Travel/photos/processed/thumbnails/cairo/pyramids/sunrise/img-1234.webp
```

If a new original subfolder is created:

```text
originals/xxxxx/
```

the application must automatically create:

```text
processed/website/xxxxx/
processed/social/xxxxx/
processed/thumbnails/xxxxx/
```

When 4:5 social output is enabled, also create:

```text
processed/social-4x5/xxxxx/
```

The folder structure must be derived from the original file's path relative to the configured `originals` directory.

Example relative source path:

```text
luxor/karnak/columns/photo-001.jpg
```

Derived output paths:

```text
processed/website/luxor/karnak/columns/photo-001.webp
processed/social/luxor/karnak/columns/photo-001.jpg
processed/thumbnails/luxor/karnak/columns/photo-001.webp
```

Rules:

- Preserve all original subfolder names exactly by default.
- Never flatten all images into one output directory.
- Never mirror the top-level `originals` folder itself inside output folders.
- Create missing derivative subfolders automatically.
- Sanitize only invalid filesystem characters when required.
- Record both the original relative path and each derivative relative path in SQLite.
- The output filename may change extension and may be normalized according to filename rules.
- Folder names must not be renamed automatically after publishing.
- Existing published derivative paths must remain stable unless explicitly migrated.
- Empty original folders do not need to be mirrored until they contain a processable image.
- A moved original should be detected and handled as a path change, not silently duplicated.

This mirrored layout is required because the same photo library will be published to:

- WordPress
- Facebook
- Instagram

The local folder layout should remain predictable for later upload, synchronization, and media-management workflows.

## 5.2 Publishing targets

The first stable version remains local-first, but every processed file must be prepared for these targets:

### WordPress

Use files from:

```text
processed/website/
```

Default format:

```text
WebP
```

Default longest edge:

```text
1920 px
```

The mirrored folder path must be stored in SQLite so a later WordPress integration can map local categories or collections to media-library metadata, posts, galleries, or custom folders.

Do not assume WordPress itself preserves local folders in its physical upload directory. Preserve the folder hierarchy locally and store it as structured metadata for future publishing.

### Facebook and Instagram

Use files from:

```text
processed/social/
```

Default format:

```text
JPEG
```

Default longest edge:

```text
1440 px
```

Because Facebook and Instagram are connected, one general social derivative may be reused for both platforms.

Optional portrait feed output:

```text
processed/social-4x5/
```

Default size:

```text
1080 × 1350 px
```

The application must not upload automatically in the first version. It must only prepare files and preserve their relative structure for later Meta publishing.


---

# 6. Application Repository Structure

Create the source-code repository with this structure:

```text
access-egypt-photo-pipeline/
├── README.md
├── LICENSE
├── pyproject.toml
├── .gitignore
├── config.example.json
├── src/
│   └── access_egypt_photos/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── config.py
│       ├── database.py
│       ├── models.py
│       ├── scanner.py
│       ├── hashing.py
│       ├── metadata.py
│       ├── processor.py
│       ├── image_operations.py
│       ├── watermark.py
│       ├── filenames.py
│       ├── reporting.py
│       ├── validation.py
│       ├── logging_setup.py
│       ├── exceptions.py
│       └── migrations/
│           ├── __init__.py
│           └── schema_v1.sql
├── tests/
│   ├── conftest.py
│   ├── test_config.py
│   ├── test_database.py
│   ├── test_hashing.py
│   ├── test_scanner.py
│   ├── test_filenames.py
│   ├── test_image_operations.py
│   ├── test_processor.py
│   └── fixtures/
├── scripts/
│   ├── install_exiftool_macos.sh
│   ├── backup_database.sh
│   └── verify_environment.py
└── docs/
    ├── installation.md
    ├── configuration.md
    ├── commands.md
    ├── workflow.md
    ├── recovery.md
    └── database-schema.md
```

---

# 7. Required Features

The first stable version must:

1. Scan photos recursively
2. Calculate SHA-256 hashes
3. Detect exact duplicates
4. Read EXIF, IPTC, and XMP metadata
5. Store records in SQLite
6. Track scan and processing status
7. Generate website images
8. Generate one shared social-media image for Facebook and Instagram
9. Optionally generate 4:5 social crops
10. Generate thumbnails
11. Strip GPS from public outputs
12. Keep private GPS in SQLite
13. Embed copyright metadata
14. Add optional visible watermarks
15. Generate deterministic filenames
16. Resume interrupted processing
17. Validate outputs
18. Export CSV reports
19. Maintain processing logs
20. Back up and validate the database
21. Support dry-run mode
22. Continue after individual image failures
23. Never overwrite valid output silently
24. Detect changed or missing originals
25. Work on macOS first while remaining portable

---

# 8. CLI Name

Expose this executable:

```bash
aep
```

In `pyproject.toml`:

```toml
[project.scripts]
aep = "access_egypt_photos.cli:app"
```

---

# 9. CLI Commands

## 9.1 Initialize the library

```bash
aep init --root "/Users/shereefelias/Documents/Access Egypt Travel/photos"
```

This command must:

- Create all required folders except `originals`
- Create `config.json`
- Create `database/photos.db`
- Run schema migrations
- Verify permissions
- Check whether ExifTool is installed
- Refuse unsafe directory layouts
- Not process any photos

---

## 9.2 Verify the environment

```bash
aep doctor
```

Check:

- Python version
- Pillow availability
- SQLite availability
- ExifTool availability and version
- Configuration validity
- Read permission for originals
- Write permission for outputs
- Database connectivity
- Disk space
- Watermark availability
- Unsafe folder overlap
- Optional RAW support
- Optional HEIC support

Display each result as:

- PASS
- WARNING
- FAILURE

Exit nonzero for critical failures.

---

## 9.3 Scan photos

```bash
aep scan
```

Examples:

```bash
aep scan --dry-run
aep scan --recursive
aep scan --workers 4
aep scan --input "/Users/shereefelias/Documents/Access Egypt Travel/photos/originals"
aep scan --include "*.jpg"
aep scan --include "*.cr3"
aep scan --exclude "exports/*"
```

Scanning must:

- Discover supported image files
- Skip hidden and temporary files
- Read file size and timestamps
- Calculate SHA-256
- Read image dimensions
- Read metadata
- Add new records
- Update changed records carefully
- Detect exact duplicates
- Record damaged files as errors
- Avoid duplicate database rows on repeated scans
- Not generate derivatives

---

## 9.4 Process photos

```bash
aep process --new
```

Examples:

```bash
aep process --all
aep process --new
aep process --status pending
aep process --id 125
aep process --limit 100
aep process --workers 4
aep process --dry-run
aep process --force
aep process --website-only
aep process --social-only
aep process --thumbnail-only
aep process --no-watermark
```

Processing must:

- Verify source existence
- Verify the original hash
- Apply EXIF orientation
- Convert to sRGB where possible
- Generate configured derivatives
- Write copyright metadata
- Strip sensitive metadata
- Apply watermark when enabled
- Validate each derivative
- Calculate derivative hashes
- Update SQLite only after successful atomic rename
- Skip valid existing outputs unless `--force`
- Continue after individual failures
- Resume after interruption

---

## 9.5 List records

```bash
aep list
```

Examples:

```bash
aep list --status failed
aep list --year 2026
aep list --location Luxor
aep list --published false
aep list --duplicate true
aep list --limit 50
aep list --format json
aep list --format csv
```

Default terminal output must not show exact GPS coordinates.

---

## 9.6 Show one record

```bash
aep show 125
```

Display:

- Original path
- Original SHA-256
- File size
- Dimensions
- Capture date
- Camera
- Lens
- GPS presence
- Country
- Region
- City
- Location name
- Title
- Caption
- Keywords
- Processing status
- Derivative paths
- Errors
- Publication flags
- Copyright status

Only show GPS coordinates with:

```bash
aep show 125 --include-private-location
```

---

## 9.7 Reprocess

```bash
aep reprocess 125
aep reprocess --failed
aep reprocess --missing-outputs
```

---

## 9.8 Validate outputs

```bash
aep validate
```

Validation must check:

- File exists
- File is readable
- Dimensions match configuration
- Hash matches database
- GPS is absent
- Sensitive serial fields are absent
- Copyright metadata is present
- Watermark is applied when expected
- Source has not changed
- Output is not unexpectedly larger than the source

---

## 9.9 Export reports

```bash
aep export csv
aep export copyright
aep export errors
aep export duplicates
```

Example:

```bash
aep export copyright \
  --output "/Users/shereefelias/Documents/Access Egypt Travel/photos/reports/copyright-2026.csv"
```

---

## 9.10 Database commands

```bash
aep db status
aep db backup
aep db vacuum
aep db integrity-check
```

Backups should be saved under:

```text
/Users/shereefelias/Documents/Access Egypt Travel/photos/backups
```

Example backup filename:

```text
photos-2026-06-23-143000.db
```

Never overwrite an existing backup.

---

## 9.11 Clean orphaned outputs

```bash
aep clean --dry-run
aep clean --orphans
aep clean --failed-partials
```

Cleaning must never delete originals.

Actual deletion must require explicit confirmation unless `--yes` is supplied.

---

# 10. Default Configuration

Create:

```text
/Users/shereefelias/Documents/Access Egypt Travel/photos/config.json
```

Use this starting configuration:

```json
{
  "schema_version": 1,
  "library": {
    "root": "/Users/shereefelias/Documents/Access Egypt Travel/photos",
    "originals_directory": "originals",
    "processed_directory": "processed",
    "preserve_relative_subfolders": true,
    "database_path": "database/photos.db",
    "reports_directory": "reports",
    "logs_directory": "logs",
    "backups_directory": "backups"
  },
  "identity": {
    "creator": "Shereef Elias",
    "copyright_owner": "Access Egypt Travel",
    "copyright_notice": "© 2026 Access Egypt Travel. All rights reserved.",
    "website_url": "",
    "contact_email": "",
    "credit_line": "Photo by Access Egypt Travel",
    "usage_terms": "No reproduction, redistribution, commercial use, or AI training without written permission."
  },
  "scanner": {
    "recursive": true,
    "follow_symbolic_links": false,
    "supported_extensions": [
      ".jpg",
      ".jpeg",
      ".png",
      ".tif",
      ".tiff",
      ".webp",
      ".heic",
      ".dng",
      ".cr2",
      ".cr3",
      ".nef",
      ".arw",
      ".orf",
      ".raf"
    ],
    "ignore_hidden_files": true,
    "ignore_patterns": [
      ".DS_Store",
      "Thumbs.db",
      "*.tmp",
      "*.part",
      "*.partial",
      "processed/**"
    ],
    "hash_algorithm": "sha256",
    "workers": 4
  },
  "outputs": {
    "website": {
      "enabled": true,
      "directory": "processed/website",
      "format": "webp",
      "max_width": 1920,
      "max_height": 1920,
      "quality": 82,
      "preserve_aspect_ratio": true,
      "prevent_upscaling": true,
      "strip_gps": true,
      "embed_copyright": true,
      "watermark": true
    },
    "social": {
      "enabled": true,
      "directory": "processed/social",
      "format": "jpeg",
      "max_width": 1440,
      "max_height": 1440,
      "quality": 88,
      "background": "#ffffff",
      "preserve_aspect_ratio": true,
      "prevent_upscaling": true,
      "strip_gps": true,
      "embed_copyright": true,
      "watermark": true
    },
    "social_4x5": {
      "enabled": false,
      "directory": "processed/social-4x5",
      "format": "jpeg",
      "width": 1080,
      "height": 1350,
      "quality": 88,
      "crop_mode": "center",
      "strip_gps": true,
      "embed_copyright": true,
      "watermark": true
    },
    "thumbnail": {
      "enabled": true,
      "directory": "processed/thumbnails",
      "format": "webp",
      "width": 400,
      "height": 400,
      "quality": 75,
      "crop_mode": "fit",
      "strip_all_sensitive_metadata": true,
      "watermark": false
    }
  },
  "watermark": {
    "enabled": true,
    "type": "image",
    "image_path": "watermark/access-egypt-watermark.png",
    "text": "© Access Egypt Travel",
    "position": "bottom-right",
    "relative_width_percent": 18,
    "opacity_percent": 65,
    "margin_percent": 2,
    "minimum_image_width": 600
  },
  "metadata": {
    "use_exiftool": true,
    "preserve_capture_date": true,
    "preserve_orientation": true,
    "store_private_gps_in_database": true,
    "strip_gps_from_public_outputs": true,
    "strip_serial_numbers_from_public_outputs": true,
    "strip_owner_name_from_public_outputs": false,
    "embed_iptc": true,
    "embed_xmp": true
  },
  "filenames": {
    "strategy": "date-location-sequence",
    "lowercase": true,
    "replace_spaces_with": "-",
    "maximum_length": 120,
    "include_short_hash": true,
    "short_hash_length": 10,
    "fallback_prefix": "access-egypt-photo"
  },
  "processing": {
    "workers": 4,
    "continue_on_error": true,
    "atomic_writes": true,
    "temporary_extension": ".partial",
    "verify_outputs": true,
    "calculate_output_hashes": true,
    "minimum_free_disk_space_gb": 5,
    "batch_size": 100
  },
  "logging": {
    "level": "INFO",
    "console": true,
    "file": true,
    "rotate_mb": 20,
    "backup_count": 10
  },
  "optional_analysis": {
    "blur_detection": false,
    "perceptual_duplicate_detection": false,
    "ai_captioning": false,
    "ai_keywording": false,
    "external_uploads_allowed": false
  }
}
```

---

# 11. SQLite Database Design

Use SQLite with:

- Foreign keys enabled
- WAL mode where appropriate
- Busy timeout configured
- UTC timestamps stored in ISO 8601
- Schema migrations
- Controlled batch commits
- One safe database-writer strategy

Do not store image binaries in SQLite.

## 11.1 Photos table

```sql
CREATE TABLE photos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_path TEXT NOT NULL UNIQUE,
    original_filename TEXT NOT NULL,
    original_relative_path TEXT NOT NULL,
    original_parent_relative_path TEXT NOT NULL,
    original_extension TEXT,
    original_size_bytes INTEGER,
    original_sha256 TEXT NOT NULL,
    perceptual_hash TEXT,
    mime_type TEXT,
    image_format TEXT,
    width INTEGER,
    height INTEGER,
    orientation INTEGER,
    color_mode TEXT,
    capture_datetime TEXT,
    capture_timezone TEXT,
    file_created_datetime TEXT,
    file_modified_datetime TEXT,
    camera_make TEXT,
    camera_model TEXT,
    camera_serial_number TEXT,
    lens_model TEXT,
    lens_serial_number TEXT,
    focal_length TEXT,
    aperture TEXT,
    shutter_speed TEXT,
    iso INTEGER,
    gps_latitude REAL,
    gps_longitude REAL,
    gps_altitude REAL,
    gps_is_private INTEGER NOT NULL DEFAULT 1,
    country TEXT,
    region TEXT,
    city TEXT,
    location_name TEXT,
    title TEXT,
    caption TEXT,
    keywords_json TEXT,
    creator TEXT,
    copyright_owner TEXT,
    copyright_notice TEXT,
    source_status TEXT NOT NULL DEFAULT 'available',
    scan_status TEXT NOT NULL DEFAULT 'pending',
    processing_status TEXT NOT NULL DEFAULT 'pending',
    is_exact_duplicate INTEGER NOT NULL DEFAULT 0,
    duplicate_of_photo_id INTEGER,
    is_published_website INTEGER NOT NULL DEFAULT 0,
    is_published_social INTEGER NOT NULL DEFAULT 0,
    copyright_registered INTEGER NOT NULL DEFAULT 0,
    copyright_registration_number TEXT,
    first_publication_date TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    last_scanned_at TEXT,
    last_processed_at TEXT,
    FOREIGN KEY (duplicate_of_photo_id) REFERENCES photos(id)
);
```

Indexes:

```sql
CREATE INDEX idx_photos_relative_path
ON photos(original_relative_path);

CREATE INDEX idx_photos_sha256
ON photos(original_sha256);

CREATE INDEX idx_photos_capture_datetime
ON photos(capture_datetime);

CREATE INDEX idx_photos_processing_status
ON photos(processing_status);

CREATE INDEX idx_photos_location
ON photos(country, region, city);

CREATE INDEX idx_photos_publication
ON photos(is_published_website, is_published_social);
```

## 11.2 Derivatives table

```sql
CREATE TABLE derivatives (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    photo_id INTEGER NOT NULL,
    derivative_type TEXT NOT NULL,
    output_path TEXT NOT NULL UNIQUE,
    output_relative_path TEXT NOT NULL,
    source_relative_path TEXT NOT NULL,
    output_format TEXT NOT NULL,
    width INTEGER,
    height INTEGER,
    size_bytes INTEGER,
    sha256 TEXT,
    processing_status TEXT NOT NULL DEFAULT 'pending',
    watermark_applied INTEGER NOT NULL DEFAULT 0,
    gps_removed INTEGER NOT NULL DEFAULT 0,
    copyright_embedded INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    last_verified_at TEXT,
    error_message TEXT,
    FOREIGN KEY (photo_id) REFERENCES photos(id) ON DELETE CASCADE,
    UNIQUE(photo_id, derivative_type)
);
```

## 11.3 Processing events table

```sql
CREATE TABLE processing_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT,
    photo_id INTEGER,
    derivative_id INTEGER,
    event_type TEXT NOT NULL,
    status TEXT NOT NULL,
    message TEXT,
    details_json TEXT,
    duration_ms INTEGER,
    created_at TEXT NOT NULL,
    FOREIGN KEY (photo_id) REFERENCES photos(id),
    FOREIGN KEY (derivative_id) REFERENCES derivatives(id)
);
```

## 11.4 Scan runs table

```sql
CREATE TABLE scan_runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id TEXT NOT NULL UNIQUE,
    started_at TEXT NOT NULL,
    finished_at TEXT,
    input_path TEXT NOT NULL,
    discovered_count INTEGER NOT NULL DEFAULT 0,
    new_count INTEGER NOT NULL DEFAULT 0,
    unchanged_count INTEGER NOT NULL DEFAULT 0,
    duplicate_count INTEGER NOT NULL DEFAULT 0,
    error_count INTEGER NOT NULL DEFAULT 0,
    status TEXT NOT NULL
);
```

## 11.5 Schema migrations table

```sql
CREATE TABLE schema_migrations (
    version INTEGER PRIMARY KEY,
    applied_at TEXT NOT NULL
);
```

---

# 12. Processing Pipeline

For every image:

1. Discover source file
2. Calculate the source path relative to `originals`
3. Recreate the source parent folder under each enabled output root
4. Preserve the relative folder structure for website, social, 4:5, and thumbnail derivatives
5. Resolve and validate path
6. Confirm source is inside originals
7. Read file metadata
8. Calculate SHA-256
9. Check for duplicate records
10. Insert or update catalog record
11. Verify source hash before processing
12. Load source without write access
13. Apply EXIF orientation
14. Convert to sRGB when possible
15. Create website derivative in the mirrored website folder
16. Create social derivative in the mirrored social folder
17. Create optional 4:5 derivative in the mirrored social-4x5 folder
18. Create thumbnail in the mirrored thumbnails folder
19. Strip GPS and sensitive metadata
20. Embed copyright metadata
21. Apply visible watermark if enabled
22. Validate output
23. Calculate output hash
24. Atomically rename temporary output
25. Update SQLite
26. Add processing event
27. Continue to the next image

The relative folder path must be stable and deterministic.

Previous generic sequence retained for reference:

2. Resolve and validate path
3. Confirm source is inside originals
4. Read file metadata
5. Calculate SHA-256
6. Check for duplicate records
7. Insert or update catalog record
8. Verify source hash before processing
9. Load source without write access
10. Apply EXIF orientation
11. Convert to sRGB when possible
12. Create website derivative
13. Create social derivative
14. Create optional 4:5 derivative
15. Create thumbnail
16. Strip GPS and sensitive metadata
17. Embed copyright metadata
18. Apply visible watermark if enabled
19. Validate output
20. Calculate output hash
21. Atomically rename temporary output
22. Update SQLite
23. Add processing event
24. Continue to the next image

---

# 13. Atomic Output Rules

Output creation must use:

```text
filename.webp.partial
```

Process:

1. Write the temporary file
2. Flush and close it
3. Confirm it is readable
4. Validate dimensions
5. Verify GPS removal
6. Verify metadata
7. Calculate SHA-256
8. Rename atomically
9. Update database only after success

Never leave a successful database record pointing to a missing final file.

---

# 14. Image Processing Rules

## Orientation

Apply EXIF orientation before resizing, cropping, or watermarking.

Final outputs should use normal pixel orientation and should not require an orientation flag.

## Resizing

Use Pillow LANCZOS.

Do not upscale unless configuration explicitly enables it.

Preserve aspect ratio except for explicit crop outputs.

## Color

Convert derivatives to sRGB where possible.

Malformed profiles should produce a warning, not a total job failure.

## JPEG

- Handle RGBA and transparent images safely
- Use configured background
- Optimize output
- Use progressive encoding when appropriate
- Apply configured quality
- Strip private metadata
- Preserve copyright metadata

## WebP

- Use configured quality
- Support lossless configuration in the future
- Validate metadata support
- Verify dimensions and readability

## HEIC

Use optional `pillow-heif`.

When unavailable:

- Catalog the file
- Mark it unsupported for processing
- Display installation instructions

## RAW

Preferred:

- Use optional `rawpy`

Fallback:

- Use an embedded preview through ExifTool when possible

Otherwise:

- Catalog the source
- Mark it unsupported for derivative generation
- Do not treat this as data loss

---

# 15. Filename Strategy

Generate deterministic filenames such as:

```text
2026-06-15-luxor-karnak-temple-a3f83c72d1.webp
```

Rules:

- Lowercase
- Replace spaces with hyphens
- Remove unsafe characters
- Collapse repeated separators
- Transliterate Unicode where practical
- Avoid Windows reserved filenames
- Include capture date when available
- Include location or title when available
- Include short SHA-256 suffix
- Keep under configured length
- Do not change published filenames automatically

Fallback:

```text
access-egypt-photo-20260615-a3f83c72d1.webp
```

---

# 16. Duplicate Handling

## Exact duplicates

Exact duplicates share the same SHA-256.

Rules:

- Keep a canonical record
- Link duplicate records to the canonical record
- Do not process exact duplicates repeatedly by default
- Never delete duplicate originals automatically
- Allow future manual review
- Support `--process-duplicates` as an override

## Perceptual duplicates

Optional only.

Use perceptual hashing to identify visually similar images.

Never automatically merge, move, or delete them.

---

# 17. Metadata Policy

The private SQLite catalog may retain:

- GPS coordinates
- Camera serial number
- Lens serial number
- Capture time
- Full camera and lens data
- Original metadata
- Processing history

Public outputs must remove:

- GPS latitude
- GPS longitude
- GPS altitude
- Camera serial number
- Lens serial number
- Embedded thumbnails that expose private metadata
- Editing-history fields where practical
- Private owner identifiers not required for copyright

Public outputs should include:

- Creator: John Gamil Gadalla
- Copyright owner: John Gamil Gadalla
- Copyright notice
- Credit line
- Website URL: https://accessegypttravel.com
- Contact email: info@accessegypttravel.com
- Usage terms
- Caption
- Keywords
- Capture date when appropriate

After writing metadata, re-read the derivative and verify that sensitive fields are absent.

---

# 18. Watermarking

Support image and text watermarks.

## Image watermark

- Transparent PNG
- Scale relative to output width
- Preserve aspect ratio
- Configurable opacity
- Configurable margin
- Configurable position
- Skip small outputs
- Avoid enlarging beyond source resolution unless enabled

Supported positions:

```text
top-left
top-center
top-right
center-left
center
center-right
bottom-left
bottom-center
bottom-right
```

## Text watermark

Support:

- Copyright text
- Configurable font path
- Relative font size
- Opacity
- Shadow or outline
- Position
- Margin

Do not package proprietary fonts.

---

# 19. Status Values

Photo status:

```text
pending
processing
complete
partial
failed
skipped
unsupported
source_missing
source_changed
```

Derivative status:

```text
pending
processing
complete
failed
missing
invalid
```

When the program starts, stale `processing` records from an interrupted run should be checked and safely reset to `pending` or `partial`.

---

# 20. Error Handling

Create these exceptions:

```text
ConfigurationError
DatabaseError
SourceFileMissingError
SourceFileChangedError
UnsupportedFormatError
MetadataReadError
MetadataWriteError
ImageProcessingError
OutputValidationError
UnsafePathError
InsufficientDiskSpaceError
```

Suggested exit codes:

```text
0 = success
1 = completed with image-level errors
2 = invalid CLI arguments
3 = configuration failure
4 = database failure
5 = missing environment dependency
6 = unsafe path or safety violation
```

Do not print private GPS values in normal errors.

---

# 21. Logging

Create:

```text
/Users/shereefelias/Documents/Access Egypt Travel/photos/logs/aep.log
/Users/shereefelias/Documents/Access Egypt Travel/photos/logs/aep-errors.log
```

Logs should rotate.

Each event should include:

- Timestamp
- Run ID
- Photo ID
- Original path
- Derivative type
- Operation
- Status
- Duration
- Error category
- Safe message

Raw GPS should only appear in explicit debug mode.

---

# 22. Performance Requirements

For 5,000 or more photos:

- Use bounded concurrency
- Avoid unbounded task queues
- Close images promptly
- Avoid loading many full-resolution images at once
- Use controlled database transactions
- Configure SQLite busy timeout
- Use WAL mode where appropriate
- Keep database writing thread-safe
- Use configurable batch size
- Support Ctrl+C cleanly
- Resume after interruption
- Show progress with Rich
- Display processed, skipped, failed, and remaining counts
- Do not display unreliable time estimates as guaranteed completion times

---

# 23. Dry-Run Requirements

Commands that write or delete files must support:

```bash
--dry-run
```

Dry-run may show:

- Files that would be scanned
- Records that would be inserted
- Records that would be updated
- Derivatives that would be generated
- Duplicates that would be flagged
- Orphans that would be deleted

Dry-run must not:

- Change SQLite
- Create final derivatives
- Delete files
- Rename files
- Modify originals
- Write metadata to images

---

# 24. Reports

## General catalog CSV

Columns:

```text
photo_id
original_filename
original_path
sha256
capture_datetime
country
region
city
location_name
title
caption
keywords
width
height
camera_make
camera_model
website_output
social_output
thumbnail_output
processing_status
published_website
published_social
copyright_registered
copyright_registration_number
first_publication_date
```

## Copyright preparation CSV

Columns:

```text
photo_id
title
original_filename
capture_datetime
first_publication_date
published_status
author
copyright_claimant
copyright_owner
country_of_origin
registration_status
registration_number
notes
```

This report is an internal preparation and inventory file. Do not claim that it is automatically accepted by any copyright office.

## Error CSV

Columns:

```text
photo_id
original_path
operation
error_type
error_message
created_at
resolved
```

## Duplicate CSV

Columns:

```text
canonical_photo_id
canonical_path
duplicate_photo_id
duplicate_path
sha256
size_bytes
```

---

# 25. Testing Requirements

Use pytest.

Test:

- Configuration validation
- Exact root-path handling with spaces
- Unsafe path rejection
- Originals never modified
- SHA-256 stability
- Duplicate detection
- Deterministic filenames
- Mirrored relative folder paths
- Nested source folders
- New source subfolders automatically creating matching derivative folders
- Filename collision handling
- Unicode filenames
- EXIF orientation
- Resize dimensions
- No upscaling
- JPEG transparency conversion
- Watermark placement
- Watermark scaling
- GPS removal
- Serial-number removal
- Copyright metadata
- Interrupted-run recovery
- Atomic writes
- Database migrations
- Database integrity
- Resume behavior
- Dry-run no-op behavior
- Missing sources
- Changed sources
- Output validation
- CSV exports
- Repeated scans
- Repeated processing
- Forced processing

Generate small test images programmatically.

Mark ExifTool tests:

```bash
pytest -m exiftool
```

Default tests must run without ExifTool installed.

---

# 26. Integration Test Dataset

Create an automated integration test library containing:

- 10 JPEG images
- 2 transparent PNG images
- 1 TIFF
- 1 EXIF-oriented image
- 1 GPS-tagged image
- 2 exact duplicates
- 1 damaged image
- 1 unsupported file
- 1 filename with spaces
- 1 Unicode filename

Verify:

- Valid images are cataloged
- Damaged images are recorded as errors
- Unsupported files are clearly ignored or reported
- Duplicates are linked
- Public outputs are generated
- GPS is removed
- Serial numbers are removed
- Copyright metadata is embedded
- Filenames are safe
- Original hashes remain unchanged
- Second run skips completed outputs
- Forced run recreates outputs
- Dry-run changes nothing
- Reports are valid

---

# 27. Packaging

Use `pyproject.toml`.

Example installation:

```bash
cd "/Users/shereefelias/Documents/Access Egypt Travel"

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -e ".[dev]"
```

Optional extras:

```toml
[project.optional-dependencies]
raw = ["rawpy"]
heic = ["pillow-heif"]
analysis = ["opencv-python", "ImageHash"]
dev = ["pytest", "pytest-cov", "ruff", "mypy"]
```

---

# 28. macOS ExifTool Installation

Install with Homebrew:

```bash
brew install exiftool
```

Verify:

```bash
exiftool -ver
```

The application must also check ExifTool through:

```bash
aep doctor
```

Use subprocess argument arrays, never shell strings built from filenames.

---

# 29. Quick Start After Implementation

```bash
cd "/Users/shereefelias/Documents/Access Egypt Travel"

python3 -m venv .venv
source .venv/bin/activate

pip install -e ".[dev,heic,raw]"

aep init \
  --root "/Users/shereefelias/Documents/Access Egypt Travel/photos"

aep doctor

aep scan --dry-run
aep scan

aep process --new --dry-run
aep process --new

aep validate
aep export copyright
```

---

# 30. Implementation Phases

## Phase 1: Foundation

Implement:

- Package structure
- Typer CLI
- Pydantic configuration
- SQLite connection
- Schema migrations
- Logging
- `init`
- `doctor`
- Tests
- Documentation

Acceptance:

- `aep --help` works
- `aep init` creates the library
- Exact path with spaces works
- Database schema is created
- Unsafe layouts are rejected
- Tests pass
- Ruff passes
- mypy passes

## Phase 2: Scanning

Implement:

- File discovery
- Filtering
- SHA-256
- Metadata reading
- Database insertion
- Duplicate detection
- `scan`
- `list`
- `show`

Acceptance:

- Re-running scan does not duplicate unchanged records
- Exact duplicates are detected
- Original hashes do not change
- Damaged files are recorded

## Phase 3: Derivatives

Implement:

- Orientation normalization
- sRGB conversion
- Resizing
- Website WebP with mirrored source folders
- Social JPEG with mirrored source folders
- Thumbnails with mirrored source folders
- Atomic writes
- Resume logic

Acceptance:

- Outputs match configuration
- No upscaling occurs
- Existing outputs are skipped
- Interrupted runs resume safely

## Phase 4: Metadata and Watermarks

Implement:

- ExifTool integration
- GPS stripping
- Serial-number stripping
- Copyright metadata
- Image watermark
- Text watermark
- Metadata validation

Acceptance:

- Public outputs contain no GPS
- Public outputs contain no serial numbers
- Copyright metadata exists
- Originals are unchanged

## Phase 5: Validation and Reports

Implement:

- `validate`
- CSV exports
- Duplicate reports
- Error reports
- Database backups
- Integrity checks
- Cleanup commands

Acceptance:

- Missing and invalid outputs are found
- Reports are valid
- Backups are unique
- Cleanup cannot delete originals

## Phase 6: Optional Features

Only after the core is stable:

- RAW development
- HEIC support
- Perceptual duplicates
- Blur detection
- Intelligent 4:5 crops
- Local AI captions
- Local AI keywords
- WordPress publishing
- Meta publishing

Do not include optional publishing or AI features in the first stable release.

---

# 31. Instructions for Codex

Paste the following into Codex after opening the repository:

```text
Build the Access Egypt Photo Pipeline described in this specification.

The primary library root is:

/Users/shereefelias/Documents/Access Egypt Travel/photos

Treat this path as the default and correctly handle the spaces in all shell commands, path validation, tests, and documentation.

Start with Phase 1 only.

Before writing code:

1. Summarize the architecture.
2. Identify major risks.
3. List external dependencies.
4. Create the repository file tree.
5. Explain original-file safety controls.

Then implement:

- pyproject.toml
- package structure
- Typer CLI
- Pydantic configuration
- SQLite migrations
- logging
- aep init
- aep doctor
- tests
- README
- configuration documentation

Do not implement image processing yet.

Requirements:

- Produce working files, not pseudocode.
- Keep the repository runnable.
- Use pathlib.
- Use type hints.
- Add docstrings to public code.
- Never modify originals.
- Reject unsafe directory overlap.
- Support dry-run architecture from the beginning.
- Use safe subprocess argument arrays.
- Do not make external network calls.
- Do not add telemetry.
- Do not upload anything.

Before finishing:

1. Run pytest.
2. Run Ruff checks.
3. Run Ruff format check.
4. Run mypy.
5. Show the exact commands executed.
6. Summarize files created.
7. Report limitations.
8. Do not claim completion while tests fail.
```

---

# 32. Initial Terminal Setup

```bash
cd "/Users/shereefelias/Documents/Access Egypt Travel"

mkdir -p access-egypt-photo-pipeline
cd access-egypt-photo-pipeline

git init

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
```

Then start Codex:

```bash
codex
```

Paste this Markdown specification or point Codex to the file.

---

# 33. Suggested File Name

Save this document as:

```text
ACCESS_EGYPT_PHOTO_PIPELINE_SPEC.md
```

Recommended location:

```text
/Users/shereefelias/Documents/Access Egypt Travel/access-egypt-photo-pipeline/ACCESS_EGYPT_PHOTO_PIPELINE_SPEC.md
```

A second copy may also be kept at:

```text
/Users/shereefelias/Documents/Access Egypt Travel/photos/ACCESS_EGYPT_PHOTO_PIPELINE_SPEC.md
```

Do not place generated source code inside the `originals` directory.

---

# 34. Final Architectural Decision

Use:

```text
Primary catalog: SQLite
Folder strategy: Mirror every path relative to originals
Publishing targets: WordPress, Facebook, Instagram
Configuration: JSON
Reports: CSV
Main language: Python
Website output: WebP
Social output: JPEG
Thumbnail output: WebP
Hashing: SHA-256
Metadata engine: ExifTool
Website longest edge: 1920 px
Social longest edge: 1440 px
Social quality: 88
Website quality: 82
Thumbnail size: 400 px
Default workers: 4
Batch size: 100
Original GPS: untouched
Private GPS catalog: allowed
Public GPS: removed
Visible watermark: configurable
Cloud processing: disabled
AI processing: disabled by default
```

This design is suitable for the current 5,000-photo target and should scale comfortably to a substantially larger library.
