# Access Egypt Travel

Boutique Egypt travel agency targeting American customers. This repository holds the working assets, content strategy, AI automation scripts, website mockups, and competitive research for [accessegypttravel.com](https://accessegypttravel.com).

**Contact:** info@accessegypttravel.com | +1 772 782 0494  
**Social:** [Facebook](https://www.facebook.com/accessegypttravel/) · [Instagram](https://www.instagram.com/accessegypttravel/) · [TripAdvisor](https://www.tripadvisor.com/Profile/AccessEgyptTravel)

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Repository Structure](#repository-structure)
3. [Tour Packages](#tour-packages)
4. [Website & Mockups](#website--mockups)
5. [Competitor Research](#competitor-research)
6. [AI Skills (Claude)](#ai-skills-claude)
7. [Automation Scripts](#automation-scripts)
8. [Brand Assets](#brand-assets)

---

## Project Overview

Access Egypt Travel is a boutique operator competing against large global tour brands (Intrepid, G Adventures, Tauck, Gate 1). Our edge is personalization, direct guide relationships, flexible itineraries, and human-scale customer service — delivered to American travelers who want Egypt done right without the big-operator tradeoffs.

**Operations model:** Clients picked up from Cairo or Hurghada, transferred to Luxor for Nile-based tours. Coverage across all major Egypt destinations.

---

## Repository Structure

```
├── CLAUDE.md                          # AI assistant instructions and brand rules
├── README.md                          # This file
│
├── Potential Egypt Packages/          # Draft tour itineraries
│   ├── 6 days 5 nights by air.docx
│   └── 6_Days_Cairo_Luxor_v2.docx
│
├── mockup/                            # Website design and planning mockups
│   ├── website-mockup.html
│   ├── pages-mockup.html
│   ├── seo-plan.html
│   └── developer-plan.html
│
├── current_website/                   # Screenshots of live site and competitor pages
│
├── .claude/skills/                    # Claude AI skills for content workflows
│   ├── egypt-content/
│   ├── email-inquiry/
│   ├── social-post/
│   ├── tour-package/
│   └── tripadvisor-response/
│
├── generate_alt_text.py               # Bulk image alt-text generation script
├── update_media_metadata.py           # WordPress media metadata updater
│
├── Tours Pricing.xlsx                 # Current tour pricing
├── Competitor_Analysis_v3_Access_Egypt.xlsx
├── Egypt_Competitor_Comparison v2.xlsx
│
├── Entry level Luxury accommodation plan.pdf
├── Midway Luxury accommodation plan.pdf
│
├── accessegypttravel.WordPress.2026-06-06.xml  # WordPress site export (backup)
├── site_icon.png
├── Logo_Green_2.png
└── Logo_Green_3.png
```

---

## Tour Packages

Draft itineraries live in `Potential Egypt Packages/`. Current drafts:

| File | Summary |
|------|---------|
| `6 days 5 nights by air.docx` | 6-day air-based Egypt itinerary |
| `6_Days_Cairo_Luxor_v2.docx` | 6-day Cairo + Luxor itinerary (v2) |

Accommodation tiers are outlined in the PDFs:
- `Entry level Luxury accommodation plan.pdf`
- `Midway Luxury accommodation plan.pdf`

Pricing is tracked in `Tours Pricing.xlsx`.

---

## Website & Mockups

`mockup/` contains HTML planning documents for the website redesign:

| File | Purpose |
|------|---------|
| `website-mockup.html` | Full site layout mockup |
| `pages-mockup.html` | Individual page wireframes |
| `seo-plan.html` | SEO strategy and target keywords |
| `developer-plan.html` | Technical implementation plan |

`current_website/` holds screenshots of the live site and select competitor pages for reference during redesign.

---

## Competitor Research

| File | Contents |
|------|---------|
| `Competitor_Analysis_v3_Access_Egypt.xlsx` | Latest competitive analysis (v3) |
| `Egypt_Competitor_Comparison v2.xlsx` | Side-by-side package/pricing comparison |

Key competitors tracked: High End Journeys, Memphis Tours, Egypt Tours Portal, Gate 1, Yalla Tours, Emo Tours, We Know Egypt, Sheba Tours, Trafalgar, Exoticca, Magic Carpet Egypt.

---

## AI Skills (Claude)

Custom Claude Code skills in `.claude/skills/` power content workflows:

| Skill | Purpose |
|-------|---------|
| `egypt-content` | Blog posts, SEO content, destination guides |
| `email-inquiry` | Inquiry response drafts in brand voice |
| `social-post` | Facebook and Instagram captions |
| `tour-package` | Tour page copy and itinerary formatting |
| `tripadvisor-response` | Review response drafts (public-facing) |

---

## Automation Scripts

| Script | Purpose |
|--------|---------|
| `generate_alt_text.py` | Generates SEO alt text for WordPress media library images |
| `update_media_metadata.py` | Updates title, caption, and alt text for WordPress media in bulk |

---

## Brand Assets

| File | Notes |
|------|-------|
| `Logo_Green_2.png` | Primary logo (green) |
| `Logo_Green_3.png` | Logo variant |
| `site_icon.png` | WordPress favicon / site icon |

Brand voice: warm, expert, trustworthy. Always address American travelers' concerns directly — safety, USD pricing, flight logistics, US-based support. No clichés.
