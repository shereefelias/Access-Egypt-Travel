# Access Egypt Travel - Current Execution Plan

Date: 2026-06-22  
Scope: Live WordPress cleanup, tour implementation, SEO, content, and performance  
Status: This is the clean working plan. It supersedes conflicting instructions in `mockup/developer-plan.html`, `mockup/seo-plan.html`, and `mockup/seo-plan-phase3.html`.

## Read This First

This document consolidates the older developer and SEO plans into one current work order based on the live site state checked through VibeAI/WP-CLI on 2026-06-22.

Do not follow older instructions that say:

- Elementor is Free-only. The live site has Elementor Pro active.
- Install or remove WP Fastest Cache. It is not installed. LiteSpeed Cache is the active cache plugin.
- Build duplicate Elementor tour pages without considering BABE. Live tours already exist as BABE `to_book` items.
- Fix empty gray tour cards as an assumed active bug. Verify first; this appears already resolved.
- Add schema/pricing before package prices and page content are reconciled.

## Source Of Truth

Before changing tour package copy, pricing, meals, inclusions, exclusions, itinerary, highlights, accommodation, or cancellation/payment language, read and follow:

- `docs/tour_packages_rules.md`
- Package source files in `mockup/tour_packages/`
- The latest approved package mockup in `mockup/pages-mockup.html`

Owner-provided package copy is protected. Do not rewrite, shorten, combine, or "improve" it unless explicitly asked and the package rules allow it. If a live page conflicts with the rules or source files, flag the conflict first.

## Current Live Stack

Verified on 2026-06-22:

- WordPress 7.0
- PHP 8.3.30
- Theme: Triply Child 2.2.7, parent Triply
- Elementor 3.21.1
- Elementor Pro 3.7.7
- BABE Booking Plugin 1.8.24
- Rank Math SEO 1.0.272
- LiteSpeed Cache 7.8.1
- Image Optimizer by Elementor 1.7.5
- Site Kit by Google 1.181.0
- Integrate Umami 0.8.3
- Wordfence 8.2.2
- Vibe AI 1.4.0

Known live counts:

- 27 published pages
- 14 draft pages
- 41 published posts
- 18 published BABE `to_book` items
- 364 image attachments
- 186 images missing alt text
- 68 published posts/pages audited for Rank Math metadata
- 18 BABE tour items audited for Rank Math metadata

## Guiding Strategy

The website should become a trust-first sales system for American travelers considering Egypt. The strongest positioning is:

- Private or small-group Egypt tours
- Led by a real Egyptologist
- Pickup from Cairo, Hurghada, and Luxor
- Clear USD pricing
- Human support in US-friendly channels
- Direct alternative to large, generic operators

Do not spend time polishing technical SEO before the visible trust problems and demo content are fixed. Google and customers both see the live pages.

## Phase 0 - Stabilize The WordPress Foundation

Do this before redesign, SEO, or schema work.

1. Create a full backup and staging copy.
   - Backup must include database, themes, plugins, and uploads.
   - Elementor Export Kit is not enough.
   - Prefer host-level staging/backup. UpdraftPlus is acceptable if no host backup exists.

2. Resolve the Elementor Core/Pro mismatch on staging.
   - Current mismatch: Elementor core 3.21.1, Elementor Pro 3.7.7.
   - Update Pro and core in the same session so they end on compatible versions.
   - Be cautious with a major Elementor 4.x jump. Test on staging first.
   - Run Elementor database update if prompted.
   - Run Elementor -> Tools -> Regenerate CSS & Data.
   - Purge LiteSpeed Cache.

3. Re-audit key pages after the update.
   - Homepage
   - Contact
   - About Us
   - Egypt Packages
   - One BABE tour page
   - Header and footer site-wide

4. Decide on analytics before Core Web Vitals measurement.
   - Site Kit and Umami are both active.
   - Keep both only if there is a clear reason.
   - If keeping Umami, verify it is async and does not distort performance baselines.

5. Do not install another cache plugin.
   - LiteSpeed Cache is already active.
   - Configure LiteSpeed later; do not add WP Rocket, WP Fastest Cache, Smush, or ShortPixel without a reason.

## Phase 1 - Fix Visible Trust Killers

These affect conversion immediately.

1. Standardize contact details everywhere.
   - US phone: `+1 772 782 0494`
   - WhatsApp: `+20 12 014-0578`
   - WhatsApp link: `https://wa.me/20120140578`
   - Email: `info@accessegypttravel.com`
   - Booking calls: `https://cal.com/accessegypttravel/30min`

   Check at least:
   - Header/top bar
   - Footer
   - Contact page
   - Homepage pre-footer CTA
   - Mobile menu/contact canvas
   - Any hidden login/contact overlay

2. Fix malformed or placeholder links.
   - Remove `mailto:contact@example.com`.
   - Remove `http://+201201405785`.
   - Fix bad YouTube/Twitter/social placeholder links.
   - Make phone, WhatsApp, email, TripAdvisor, Facebook, Instagram clickable and correct.

3. Fix homepage positioning.
   - Rename visible page title/H1 away from "Homepage" or "Home 1".
   - Remove demo/travel-template copy such as generic "Natural beauty", "Special Offers", "Trip Coins", and similar theme remnants.
   - Add a clear hero message around private Egypt tours led by an Egyptologist.
   - Add a clear CTA: request quote, WhatsApp, or schedule call.
   - Add trust strip: pickup locations, Egyptologist-led, USD pricing, US-friendly support.

4. Fix the Contact page.
   - Replace black/broken hero.
   - Fix phone/email links.
   - Make it a multi-channel contact hub: call, WhatsApp, email, Cal.com.
   - Include pickup locations: Cairo, Hurghada, Luxor.
   - Avoid showing only "Hurghada" as the address; include the US trust address only if owner confirms it should be public.

5. Rebuild/footer cleanup.
   - Update copyright year.
   - Remove stale "At Access Egypt Travel" phrasing if it conflicts with current LLC/legal language.
   - Include key navigation columns.
   - Include social links.
   - Include contact methods.
   - Avoid duplicate contact blocks or hidden template overlays with old values.

6. Clean public demo content.
   - The live site still has demo-style posts from the Triply import.
   - Verify exact posts before trashing.
   - Prefer move to Trash, wait, then permanently delete.
   - Do not delete BABE system pages: checkout, confirmation, customer/admin confirmation, add services, my account, all items, search result.

## Phase 2 - Reconcile Tours And Booking Structure

The live site has BABE `to_book` items. Do not create duplicate tour URLs unless there is a deliberate migration plan.

Recommended path:

1. Keep BABE as the booking engine.
   - Existing URLs live under `/to_book/...`.
   - They contain booking forms and tour data.
   - Duplicating them as Elementor pages can split SEO and break booking flow.

2. Choose one implementation model.
   - Model A: Extend the BABE item pages with missing blocks.
   - Model B: Use Elementor Pro Theme Builder single template for BABE items and embed/retain booking functionality.

3. Reconcile package source data before page work.
   - Confirm live prices against package source docs and `docs/tour_packages_rules.md`.
   - Confirm which packages are the main five strategic packages.
   - Confirm how older Luxor day tours and cruise-only tours should appear relative to duration packages.

4. Add missing page blocks only after reconciliation.
   - Tour at a Glance
   - Accommodation tiers
   - Pricing and discount table
   - Payment and cancellation policy
   - Reviews/trust block
   - Sticky sub-nav
   - Breadcrumbs
   - Related tours/content links

5. Apply mandatory package rules.
   - 9-day package gets "Most Popular" only.
   - 12-day/11-night package gets "Best Value" only.
   - Use "Transportation", not "Transport".
   - Use "Entry Visa", not "Visa".
   - Guide wording: `English — other languages on request`.
   - Keep cancellation table clean with no unauthorized footnotes.
   - Use approved meals, beverage exclusions, add-ons, and overnight wording.

## Phase 3 - Navigation And Site Architecture

Do this after the tour structure is settled.

Recommended main nav:

- Home
- Tours
- Destinations
- Reviews
- FAQs
- About
- Contact
- Optional: Pay Now, only when payment workflow is ready

Recommended footer groups:

- Tours
- Traveler Resources
- Company
- Contact
- Legal

Do not feature Blog in the main nav until the demo posts are removed and content strategy is active. A blog can exist quietly for SEO content, but it should not be a primary visitor path yet.

Important slug decisions:

- Current Luxor page uses `/tour/`, which is weak. Do not change without 301 redirects.
- Existing page slugs such as `/egypt-packages/`, `/nile-cruise/`, `/tailor-made/`, `/about-us/`, and `/contact/` can stay.
- New content pages should use simple slugs such as `/egypt-visa-requirements-for-americans/`, `/is-egypt-safe-for-americans/`, `/hurghada-to-luxor-day-trip/`, `/best-time-to-visit-egypt/`, `/what-to-pack-for-egypt/`, `/cairo-to-luxor-tour/`.

## Phase 4 - Rank Math SEO Setup

Do this after visible demo content and structural problems are cleaned up.

1. Keep crawlability as-is unless new issues appear.
   - Search visibility is on.
   - `robots.txt` is acceptable.
   - Rank Math sitemap exists at `/sitemap_index.xml`.

2. Add SEO metadata to priority pages.
   - Homepage
   - Egypt Packages
   - Luxor Tours
   - Nile Cruise
   - Tailor-Made
   - About
   - Contact
   - FAQ

3. Add SEO metadata to BABE `to_book` items.
   - Current audit: all 18 `to_book` items have no explicit Rank Math title.
   - Current audit: 13 of 18 `to_book` items have no Rank Math description.
   - This is more important than polishing low-value posts because tours are the money pages.

4. Use focus keywords as guidance, not as a writing cage.
   - Do not force exact-match keywords if they make copy unnatural.
   - Prioritize trust, clarity, and conversion.

5. Keep meta descriptions specific.
   - Mention private tours, Egyptologist guide, pickup location, USD pricing, and American traveler support where relevant.
   - Keep descriptions around 120-160 characters where practical.

6. Submit sitemap only after cleanup.
   - After deleting/trashing demo URLs and updating priority pages, submit `/sitemap_index.xml` in Google Search Console.
   - Use Search Console Removals for junk URLs only after they are actually removed/noindexed/redirected.

## Phase 5 - Content Pages For Organic Traffic

Build these as real helpful resources, not generic blog filler.

Priority pages:

1. Egypt Visa Requirements for American Citizens
2. Is Egypt Safe for American Tourists?
3. Hurghada to Luxor Day Tours - Complete Guide
4. Best Time to Visit Egypt
5. What to Pack for Egypt
6. Cairo to Luxor: Your Complete Tour Guide

Rules for these pages:

- Write for American travelers.
- Address concerns directly.
- Include John Gamil's real experience where appropriate.
- Include current source citations for visas, safety advisories, flights, and other unstable facts.
- Add CTA blocks linking to relevant tours/contact.
- Add internal links to money pages.
- Add visible author/byline and last-updated date.
- Do not make unsupported safety claims.
- Do not quote prices unless confirmed.

## Phase 6 - Image SEO And Media Cleanup

1. Check Image Optimizer settings first.
   - Image Optimizer by Elementor is already active.
   - Do not install Smush or ShortPixel unless the existing plugin cannot do the job.

2. Fix missing alt text.
   - Current audit: 186 of 364 images are missing alt text.
   - Use `generate_alt_text.py` and `update_media_metadata.py` only after reviewing credentials/session requirements.
   - Spot-check generated alt text manually.

3. Prioritize images that appear on:
   - Homepage
   - Tour cards
   - Tour pages
   - About page
   - Contact page
   - Destination/content pages

4. Set social preview images.
   - Use Rank Math Social tab.
   - Avoid defaulting to logo for all pages.
   - Use real Egypt/tour imagery, 1200px wide where possible.

## Phase 7 - Schema

Add schema only after page content and metadata are stable.

Recommended schema:

- Organization / LocalBusiness on homepage and contact, using accurate business contact data.
- Person schema for John Gamil on About page.
- BreadcrumbList via Rank Math breadcrumbs, one source only.
- Article schema for content pages.
- FAQ schema only where the exact FAQ text visibly appears on the page.
- Product/Tour/Offer schema on tour pages only after prices and inclusions are confirmed.

Important:

- Do not duplicate schema through Rank Math, theme, and manual JSON-LD at the same time.
- Do not add Product/Offer schema with outdated or disputed prices.
- Do not promise Google FAQ accordions; FAQ rich results are not guaranteed.

## Phase 8 - Performance And Core Web Vitals

Do this after Elementor has been stabilized and major layout/content edits are complete.

1. Establish baseline.
   - Test homepage and main tour page in PageSpeed Insights.
   - Test mobile first.
   - Resolve Umami/Site Kit decision before using numbers as baseline.

2. Configure LiteSpeed Cache carefully.
   - Enable cache.
   - Browser cache on.
   - Test HTML/CSS/JS minify/defer settings one at a time.
   - Purge cache after changes.
   - Test logged-out/incognito pages after each change.

3. Optimize hero/LCP images.
   - Use correctly sized images.
   - Avoid lazy loading above-the-fold hero images.
   - Add dimensions where possible.
   - Confirm hero images are real images or acceptable Elementor output, not SEO-invisible decorative backgrounds when image SEO matters.

4. Avoid plugin bloat.
   - Do not add form, popup, schema, cache, compression, or SEO plugins unless the current stack cannot support the requirement.

## Current Top Risks

1. Elementor Core/Pro mismatch can cause broken rendering and unreliable design work.
2. Live demo content damages trust and SEO.
3. Contact links and phone formatting are inconsistent.
4. BABE tours and proposed Elementor pages can become duplicate competing URLs if not handled carefully.
5. Tour pricing/source conflicts must be resolved before schema, search snippets, or public package tables.
6. Most money pages lack explicit Rank Math metadata.
7. Image alt text coverage is incomplete.
8. Dual analytics can distort performance testing.

## Decisions Needed From Owner

1. Confirm current prices for the five main duration packages.
2. Confirm whether the 12-day/11-night package is the final "Best Value" package name and duration.
3. Confirm whether the public US address should appear on the site.
4. Decide whether to keep Umami alongside Site Kit.
5. Decide whether payment page should be public now or wait until PayPal/Square are live.
6. Confirm whether BABE `to_book` URLs remain canonical tour pages or whether a migration to Elementor templates is planned.

## Working Rule For Future Tasks

When in doubt, use this order:

1. Protect approved tour copy.
2. Preserve booking functionality.
3. Fix visible trust issues.
4. Make pages useful to American travelers.
5. Add SEO metadata.
6. Add schema/performance polish after content is stable.

Do not let SEO tools, plugin suggestions, or page-builder convenience override the business goal: help an American traveler trust Access Egypt Travel enough to ask a real person about a private Egypt trip.
