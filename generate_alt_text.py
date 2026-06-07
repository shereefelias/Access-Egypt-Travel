"""
generate_alt_text.py

Logs into the WordPress media library, iterates every image in the grid,
and clicks "Generate Alt text" for any image whose Alternative Text field is empty.

Requirements:
    pip install playwright
    playwright install webkit        ← installs Safari/WebKit engine (no Chromium needed)

    Safari prerequisite (one-time):
    Safari → Develop menu → Allow Remote Automation
    (If Develop is hidden: Safari → Settings → Advanced → Show Develop menu)

Usage:
    WP_USER=admin WP_PASS=secret python generate_alt_text.py
    — or —
    python generate_alt_text.py   (will prompt for credentials)

Session is saved to .wp_session/ so you only need to log in once.
Delete that folder to force a fresh login.
"""

import asyncio
import os
import sys
import pathlib
import getpass

SESSION_DIR = pathlib.Path(__file__).parent / ".wp_session"

try:
    from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
except ImportError:
    print("Playwright not found. Run:  pip install playwright && playwright install webkit")
    sys.exit(1)

WP_URL = "https://accessegypttravel.com"

# Selectors for the alt-text input inside the attachment details sidebar.
# WordPress uses different markup depending on the view / plugins installed.
ALT_SELECTORS = [
    ".attachment-details .setting[data-setting='alt'] input",
    ".attachment-details input[name='alt']",
    "#attachment-details-two-column-alt-text",
    "#attachment-details-alt-text",
    ".media-modal .setting[data-setting='alt'] input",
]

# Selector for the AI alt-text generate button (plugin: AI Alt Text Generator)
GEN_BTN_SELECTOR = "#ai-alt-text-generate-button"


async def find_first(page, selectors):
    for sel in selectors:
        try:
            el = await page.query_selector(sel)
            if el:
                return el, sel
        except Exception:
            pass
    return None, None


async def wait_for_alt_populated(page, timeout_ms=20_000):
    """Return True once any known alt field has a non-empty value."""
    deadline = asyncio.get_event_loop().time() + timeout_ms / 1000
    while asyncio.get_event_loop().time() < deadline:
        for sel in ALT_SELECTORS:
            try:
                el = await page.query_selector(sel)
                if el:
                    val = (await el.input_value()).strip()
                    if val:
                        return val
            except Exception:
                pass
        await asyncio.sleep(0.5)
    return ""


async def main():
    username = os.environ.get("WP_USER") or input("WordPress username: ").strip()
    password = os.environ.get("WP_PASS") or getpass.getpass("WordPress password: ")

    stats = {
        "visited":        0,
        "skipped_no_img": 0,
        "has_alt":        0,
        "generated":      0,
        "no_button":      0,
        "errors":         0,
    }

    async with async_playwright() as pw:
        # Use Safari (WebKit) — requires "Allow Remote Automation" in Safari > Develop
        try:
            browser = await pw.webkit.launch(
                headless=False,
                slow_mo=200,
            )
        except Exception as e:
            print(f"Could not launch Safari/WebKit: {e}")
            print("Make sure you ran:  playwright install webkit")
            print("And enabled:  Safari → Develop → Allow Remote Automation")
            sys.exit(1)

        # Restore saved session if it exists (skips login on repeat runs)
        SESSION_DIR.mkdir(exist_ok=True)
        storage_file = SESSION_DIR / "storage_state.json"
        if storage_file.exists():
            print("Found saved session — skipping login.")
            context = await browser.new_context(storage_state=str(storage_file))
        else:
            context = await browser.new_context()

        page = await context.new_page()

        # ── Login (only if no saved session) ──────────────────────────────────
        if not storage_file.exists():
            print("Logging in …")
            await page.goto(f"{WP_URL}/wp-login.php")
            await page.fill("#user_login", username)
            await page.fill("#user_pass", password)
            await page.click("#wp-submit")
            try:
                await page.wait_for_url("**/wp-admin/**", timeout=15_000)
            except PlaywrightTimeoutError:
                print("ERROR: Login failed — check your credentials.")
                await browser.close()
                return
            # Save session so next run skips login
            await context.storage_state(path=str(storage_file))
            print(f"Logged in. Session saved to {storage_file}\n")
        else:
            await page.goto(f"{WP_URL}/wp-admin/")
            await page.wait_for_load_state("networkidle")
            # Verify the session is still valid
            if "wp-login" in page.url:
                print("Saved session expired — logging in again …")
                storage_file.unlink()
                await page.goto(f"{WP_URL}/wp-login.php")
                await page.fill("#user_login", username)
                await page.fill("#user_pass", password)
                await page.click("#wp-submit")
                try:
                    await page.wait_for_url("**/wp-admin/**", timeout=15_000)
                except PlaywrightTimeoutError:
                    print("ERROR: Login failed — check your credentials.")
                    await browser.close()
                    return
                await context.storage_state(path=str(storage_file))
                print(f"Logged in. Session saved to {storage_file}\n")
            else:
                print("Session still valid.\n")

        # ── Media Library ──────────────────────────────────────────────────────
        await page.goto(f"{WP_URL}/wp-admin/upload.php")
        await page.wait_for_load_state("networkidle")

        # Make sure we're in grid view (switch if needed)
        switch_btn = await page.query_selector("#view-switch-list")
        if switch_btn:
            grid_btn = await page.query_selector("#view-switch-grid")
            if grid_btn:
                await grid_btn.click()
                await page.wait_for_timeout(800)

        lib_page = 1

        while True:
            print(f"═══ Media page {lib_page} ═══")

            try:
                await page.wait_for_selector(".attachment", timeout=12_000)
            except PlaywrightTimeoutError:
                print("No attachments found — finished.")
                break

            # Collect stable IDs so we can re-query after each click
            attachments = await page.query_selector_all(".attachment[data-id]")
            ids = [await a.get_attribute("data-id") for a in attachments]
            print(f"Found {len(ids)} items.\n")

            for pos, att_id in enumerate(ids, start=1):
                print(f"  [{pos}/{len(ids)}]  id={att_id}", end=" … ")

                # Close any open details panel before clicking the next item
                # (the panel's preview image overlaps the grid and intercepts clicks)
                await page.keyboard.press("Escape")
                await page.wait_for_timeout(300)

                # Re-find the element by its data-id (avoids stale handles)
                el = await page.query_selector(f'.attachment[data-id="{att_id}"]')
                if not el:
                    print("not in DOM, skipping")
                    stats["errors"] += 1
                    continue

                # Skip non-image items (no <img> child = document/video)
                thumb = await el.query_selector("img")
                if not thumb:
                    print("not an image")
                    stats["skipped_no_img"] += 1
                    continue

                # Click via JS to bypass any remaining overlay interference
                await page.evaluate(f'document.querySelector(\'.attachment[data-id="{att_id}"]\').click()')
                await page.wait_for_timeout(700)

                # Wait for sidebar / modal to appear
                try:
                    await page.wait_for_selector(
                        ".attachment-details, .media-sidebar .settings",
                        timeout=6_000,
                    )
                except PlaywrightTimeoutError:
                    print("sidebar timeout")
                    stats["errors"] += 1
                    continue

                # Find alt text field
                alt_el, alt_sel = await find_first(page, ALT_SELECTORS)
                if not alt_el:
                    print("no alt field (non-image?)")
                    stats["skipped_no_img"] += 1
                    continue

                stats["visited"] += 1
                alt_value = (await alt_el.input_value()).strip()

                if alt_value:
                    print(f'has alt  ->  "{alt_value[:55]}"')
                    stats["has_alt"] += 1
                    continue

                # Alt text is empty — click the Generate button via JS
                # (button id confirmed: #ai-alt-text-generate-button)
                clicked = await page.evaluate("""
                    (() => {
                        const btn = document.querySelector('#ai-alt-text-generate-button');
                        if (btn) { btn.click(); return true; }
                        return false;
                    })()
                """)

                if not clicked:
                    print("empty — no Generate button found")
                    stats["no_button"] += 1
                    continue

                print("empty — clicking Generate …", end=" ", flush=True)

                # Wait for the API to fill in the alt text
                new_alt = await wait_for_alt_populated(page, timeout_ms=20_000)

                if new_alt:
                    print(f'done  ->  "{new_alt[:55]}"')
                    stats["generated"] += 1
                else:
                    print("generation timed out")
                    stats["errors"] += 1

                # Pause between generates to avoid hitting the AI API rate limit
                await page.wait_for_timeout(1200)

            # ── Pagination ────────────────────────────────────────────────────
            next_page = await page.query_selector(".next-page:not([disabled])")
            if next_page:
                await next_page.click()
                await page.wait_for_load_state("networkidle")
                await page.wait_for_timeout(800)
                lib_page += 1
            else:
                print("\nNo more pages.")
                break

        # ── Summary ───────────────────────────────────────────────────────────
        print("\n" + "═" * 52)
        print("FINISHED")
        print(f"  Images visited       : {stats['visited']}")
        print(f"  Already had alt text : {stats['has_alt']}")
        print(f"  Alt text generated   : {stats['generated']}")
        print(f"  No Generate button   : {stats['no_button']}")
        print(f"  Non-image / skipped  : {stats['skipped_no_img']}")
        print(f"  Errors / timeouts    : {stats['errors']}")
        print("═" * 52)

        try:
            input("\nPress Enter to close the browser …")
        except EOFError:
            pass
        await context.close()
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
