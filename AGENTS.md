# Access Egypt Travel - Codex Project Instructions

This repository is a working strategy, content, mockup, and automation workspace for Access Egypt Travel. Treat it as a live business website project, not a generic demo repo.

## Read First

Before making changes, read the relevant source-of-truth files:

- `README.md` for the repository map and business overview.
- `CLAUDE.md` for brand voice, audience, contact details, and operating rules.
- `docs/tour_packages_rules.md` before any task involving tour packages, itineraries, pricing, meals, highlights, inclusions, exclusions, or customer-facing tour copy.

The tour package rules are mandatory. If a request conflicts with them, stop and flag the conflict instead of silently changing the copy.

## Business Context

Access Egypt Travel is a boutique Egypt travel agency targeting American travelers. The positioning is personal, expert, reassuring, and specific. The business competes against large tour operators by emphasizing private or smaller tours, direct guide relationships, flexible itineraries, transparent USD pricing, and real human support.

Always keep American traveler concerns in view:

- Safety and first-timer anxiety.
- USD pricing and no hidden-fee language.
- International and domestic flight logistics.
- US-based support and fast response.
- Value compared with large group operators.

## Content Rules

- Preserve owner-provided tour package text unless the user explicitly asks for a rewrite and the package rules allow it.
- Do not abbreviate, combine, or "improve" approved package copy on your own.
- Do not quote prices unless the current source has been provided or confirmed.
- Avoid travel cliches such as "land of the pharaohs," "timeless wonders," "once in a lifetime," and "bucket list."
- Prefer concrete details over generic claims.
- Customer-facing copy should have a hook, one real differentiator, and a clear CTA.

## Project Structure

- `index.html` redirects to `mockup/`.
- `mockup/index.html` is the internal preview hub.
- `mockup/pages-mockup.html` is the main self-contained page/tour mockup with CSS and inline JavaScript.
- `mockup/developer-plan.html` documents the WordPress/Elementor implementation plan and live-site audit.
- `mockup/content/` and `mockup/Brief introductions about sites/` hold content drafts.
- `mockup/tour_packages/` holds package source documents and notes.
- `docs/accessegypttravel.WordPress.2026-06-06.xml` is the WordPress export backup.
- `generate_alt_text.py` and `update_media_metadata.py` automate WordPress media metadata work with Playwright.

## WordPress / Elementor Notes

The target live site stack is WordPress, Elementor Pro, BABE Booking Plugin, Rank Math SEO, Cal.com, and WhatsApp Business. When working on Elementor implementation guidance, prefer the existing project docs and the local `.claude/skills/elementor` guidance.

The developer plan says the tour pages already exist as BABE items, so implementation guidance should generally extend or style BABE templates rather than hand-building duplicate Elementor tour pages.

## Editing Guidelines

- Keep edits scoped and consistent with the existing static HTML style unless asked to refactor.
- This repo is deployed wholesale to GitHub Pages from `main`, so avoid adding private credentials, session files, or throwaway artifacts.
- Never commit or expose WordPress credentials, Playwright session state, API keys, or private customer information.
- Do not modify `.claude/settings.local.json` unless the user explicitly asks.

## Verification

For static HTML changes, open or serve the relevant file locally when practical and check layout across desktop and mobile widths. For Python scripts, prefer syntax checks and dry-run style review unless credentials and live-site access are intentionally provided.

