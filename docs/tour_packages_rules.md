# Access Egypt Travel — Tour Package Rules

> **READ THIS BEFORE ANY TOUR PACKAGE TASK.**
> These rules override any assumption, default behavior, or template. No exceptions.

---

## Business Info

| Field | Value |
|---|---|
| Domain | accessegypttravel.com |
| Facebook | https://www.facebook.com/accessegypttravel/ |
| Instagram | https://www.instagram.com/accessegypttravel/ |
| TripAdvisor | https://www.tripadvisor.com/Attraction_Review-g294205-d25314995-Reviews-Access_Egypt_travel-Luxor_Nile_River_Valley.html |
| US Phone | +1 772 782 0494 |
| Egypt Phone | +20 12 014-0578 (WhatsApp Business) |
| US Address | 741 Woodruff Rd, Suite 1125, Greenville, SC 29607 |
| CEO / Founder | John Gadalla |
| CFO | Hani Kamel |
| CTO | Shereef E (do not use full last name) |
| Booking calls | https://cal.com/accessegypttravel/30min |
| Website | WordPress + Elementor 3.7.7 |

---

## ⚠️ Core Rule — No Exceptions

**Do not abbreviate, combine, or change tour package text when documentation has been provided.**
The copy is already refined. If something looks off, flag it in red in the mockup with a team note — do not silently fix it or rewrite it.
This applies to: Overview, Daily Itinerary, Meals, Inclusions, and all other sections.

---

## 🏆 Package Positioning

### ⭐ Most Popular — 9 Days / 8 Nights (Cairo · Luxor · Aswan · Nile Cruise)
- Display a **"Most Popular"** badge on the 9-day tour card, page header, and any comparison grid.
- Visually distinguish the 9-day row in any side-by-side package table.

### 💰 Best Value — 11 Days / 10 Nights (Full Egypt Experience)
- Display a **"Best Value"** badge on the 11-day tour card, page header, and any comparison grid.

**Badge style in pages-mockup.html:**
Use a gold-background pill label (e.g., `background: #c49a3c; color: #fff; border-radius: 20px; padding: 3px 12px; font-size: 12px; font-weight: 600`).
Do **not** apply either label to any other package.

---

## 📋 Standardize for ALL Packages
*(Apply to 6-day, 7-day, 8-day, 9-day, and 11-day — no exceptions)*

---

### 1 — Stats Bar: Accommodation Label

The stats bar (above the overview) must include an accommodation line:

| Package Type | Label |
|---|---|
| Non-cruise (6-day, 7-day) | 🏨 Accommodation: 5-Star Hotels |
| Cruise packages (8-day, 9-day, 11-day) | 🏨 Accommodation: 5-Star Hotels & Cruise Ship |

---

### 2 — Day 1: Name Sign in Representative Greeting

Every Day 1 that references the airport meeting must include **"name sign"** — applies to ALL packages, regardless of whether the `.md` mentions it. This is a standard operational rule confirmed by owner on 2026-06-20.

✅ `"...a dedicated representative will be waiting with a name sign to greet you..."`
❌ Any version that omits "name sign"

---

### 3 — Tour at a Glance: Guide Wording

The Guide row must always read exactly:

> **English — other languages on request**

No variations: not "English speaking guide," not "licensed guide," not just "English."

---

### 4 — Tour at a Glance: Transportation Label & Format

Label: **Transportation** (not "Transport")

The row always has exactly three lines:
```
Domestic flights:          Included
Airport/Hotel Transport:   Included
Tour Transport:            Included
```

---

### 5 — Tour at a Glance: Entry Visa Label

Label: **Entry Visa** (not "Visa")
Value: Included

---

### 6 — Cancellation Table: No Footnotes

**Never add this line** (or anything like it) below the cancellation table:
> ❌ *"Note: domestic transport cancellation fees may apply in addition to the above."*

This line is unauthorized. The cancellation table ends at the 15-day penalty row. Nothing follows it.

---

### 7 — Blue Site Marking in Day Body Text

Site and city names in the day-by-day paragraphs must use the same interactive popup spans as the Overview and Highlights sections:

- **Site names** (temples, museums, monuments):
  `<span class="site-link" data-site="Karnak Temple Complex">Karnak Temple Complex</span>`
- **City names** (Cairo, Luxor, Aswan, etc.):
  `<span class="city-link" data-city="Luxor">Luxor</span>`
- When "The" is part of the official name, include it inside the span:
  `<span class="site-link" data-site="The Valley of the Kings">The Valley of the Kings</span>`

> **Status: ✅ DONE** — applied to all 5 packages (6-day, 7-day, 8-day, 9-day, 12-day) as of 2026-06-20.

---

### 8 — Highlights: Circle Color

The `.hl-num` circles were terracotta (`#b5451b`). **Change to gold:**

> `.hl-num { background: #c49a3c; }`

One CSS rule change in the `<style>` block of `pages-mockup.html` covers all packages.

> **Status: ✅ DONE** — CSS changed to `#c49a3c` in pages-mockup.html as of 2026-06-20.

---

### 9 — "Overnight in [City]"

The June 18 Notes confirmed: add `"Overnight in [City]"` at the end of each day for clarity.

**Decision: Option A — applied to ALL days across ALL packages.**

> **Status: ✅ DONE** — "Overnight in [City]" added to every day in all 5 packages as of 2026-06-20.

---

### 10 — Beverages in NOT Included (Cruise Packages)

Cruise packages include a 4th NOT-included line for beverages. All three use the same standardized wording (confirmed by owner 2026-06-20):

> **Beverages (bottled water provided only during excursions)**

Order in NOT included list: International airfare → Gratuities → Personal expenses → Beverages (always last).

Non-cruise packages (6-day, 7-day) keep exactly 3 NOT-included lines — no beverages line.

> **Status: ✅ DONE** — standardized wording applied to 8-day, 9-day, and 12-day as of 2026-06-20.

---

## 🍽️ Meals Standardization

**Standard format for all packages:**
```
Breakfast + Lunch ([X] Meals in Total)
```

**Formula:** number of meal days × 2 = total  
Example: 6-day / 5 nights = 5 × 2 = **Breakfast + Lunch (10 Meals in Total)**

**Nile Cruise meals:** always open buffet (food only)
```
All Meals — Open Buffet
```

> Nile Cruise is **NOT** all-inclusive. No drinks included — not even water.
> This is an internal constraint. Do not mention it in package copy unless it already appears in the provided `.md`.

---

## 🏺 Tomb Names

**The Valley of the Kings** — total 4 tombs = 3 regular tombs + the extraordinary tomb of **Ramesses V & VI**

**Correct phrasing (highlights & body text):** "3 tombs plus the extraordinary tomb of Ramesses V & VI"
❌ Do NOT write "4 tombs plus the extraordinary" (that implies 5 total)
- Always use Roman numerals: **Ramesses V & VI** (not "5th & 6th")
- Only the tomb of Ramesses V & VI is guaranteed open
- Other tombs may be swapped in the field if closed — handle operationally, never mention in copy
- Do not reference closures, substitutions, or ticket types in any published text

---

## 🎭 Optional Add-Ons

**Display style:** plain bullets, no icons (applies to all packages)

**6-day and 7-day (non-cruise):**
1. Dinner cruise on the Nile in Cairo *(always first)*
2. Sound & Light show at the Pyramids
3. Hot air balloon over Luxor at sunrise
4. Sound & Light Show at Karnak Temples

**8-day (cruise — 4 add-ons only, confirmed by owner 2026-06-20):**
1. Sound & Light show at the Pyramids
2. Hot air balloon over Luxor at sunrise
3. Sound & Light Show at Karnak Temples
4. Abu Simbel day trip from Aswan *(* if time allows)*
❌ Do NOT include "Dinner cruise on the Nile in Cairo" or "Sound & Light Show at Philae Temple" for the 8-day.

**9-day and 12-day (cruise — 6 add-ons):**
1. Dinner cruise on the Nile in Cairo *(always first)*
2. Sound & Light show at the Pyramids
3. Hot air balloon over Luxor at sunrise
4. Sound & Light Show at Karnak Temples
5. Sound & Light Show at Philae Temple
6. Abu Simbel Temples

**7-day correction (per June 18 Notes):**
- ❌ Remove: "Pickup from Hurghada"
- ✅ Add: "Sound & Light show at the Pyramids"

**8-day Day 5 correction (per June 18 Notes):**
- Add to Day 5 body text: *"(add-on: Abu Simbel if time allows)"*
- This is important — travelers may not book if they don't know the option exists

---

## ✨ Highlights

**Keep order of sites** — the sequence reflects the visiting order. It must be displayed as an ordered sequence.

**Display style (updated 2026-06-17):** Numbered vertical timeline (`.hl-timeline` component)
- Sequential number in a filled **gold (#c49a3c)** circle
- Thin vertical connector line behind the circles
- Single column, exact visiting order
- No emoji, no icons
- Built as `.hl-timeline` — paste into Elementor via Custom HTML block

**"The" rule:** include "The" inside the span when it's part of the official name
✅ `<span class="site-link" data-site="The Sphinx">The Sphinx</span>`
❌ `The <span class="site-link">Sphinx</span>`

**Standard site list (varies by package length):**

| # | Site |
|---|---|
| 1 | Giza Pyramids & The Sphinx *(include "The")* |
| 2 | Grand Egyptian Museum (GEM) |
| 3 | Saladin Citadel / Mohammed Ali Mosque |
| 4 | Ancient Churches of Coptic Cairo |
| 5 | National Museum of Egyptian Civilization (NMEC) — *where the royal mummies are* |
| 6 | Karnak Temple Complex |
| 7 | Luxor Temple & Sphinx Avenue *(sub-note: "Lit up at night" — own line, not inline)* |
| 8 | The Valley of the Kings (4 tombs) |
| 9 | Hatshepsut Temple |
| 10 | Deir el-Medina (Artisans' Village) |
| 11 | Colossi of Memnon |
| 12 | Felucca Ride on the Nile |

*Cruise packages also include: Edfu Temple, Kom Ombo Temple, Philae Temple, The High Dam, The Unfinished Obelisk, The Nubian Village*

---

## 📅 Daily Itinerary

- Use text exactly as provided in the `.md` file — do not abbreviate or rewrite
- If something looks wrong, flag it — do not silently fix it
- Add "Overnight in [city]" at the end of every day in every package (see Section 9 — confirmed)

---

## 🗺️ Official Names

Always use these exact names:

| Name | Notes |
|---|---|
| Cairo International Airport (CAI) | Not just "Cairo Airport" |
| Luxor Airport (LXR) | |
| Hurghada International Airport (HRG) | |
| West Bank Tour | NOT "West Bank" — avoids political confusion |
| East Bank Tour | NOT "East Bank" — same reason |
| Marriott Mena House | NOT "Mena House" or "Marriott Mina House" |

---

## 💵 Pricing

| Category | Price Per Person |
|---|---|
| Standard (double occupancy) | From [package price] |
| Single supplement | +50% of base price |
| Group of 4–7 travelers | 10% discount — Exclusive Offer |
| Group of 8+ travelers | 15% discount |

- Always state: **"All prices are quoted in USD."**
- Remove: *"Contact us for current rates."*
- **NEVER** mention "bonus inclusions" — we do not offer them. Remove any instance from all copy. *(Critical)*

---

## 💳 Payment & Cancellation Policy

> 💳 25% deposit secures your booking. Remaining full balance is due 65 days before arrival.

**When You Cancel:**

| Timing | Penalty |
|---|---|
| Any time | 25% non-refundable deposit |
| 60–31 days prior to arrival | 50% penalty |
| 30–16 days prior to arrival | 75% penalty |
| 15 days or fewer prior to arrival | 100% penalty |

**Nothing is added below this table.** No footnotes. No extra lines. (See Section 6.)

---

## 🚫 What Is NOT Included

Exactly 3 lines for all non-cruise packages:

1. International airfare
2. Gratuities for guides and drivers
3. Personal expenses — phone calls, laundry, souvenirs, etc.

*Cruise packages (8-day, 9-day, 12-day): add a 4th beverages line per Section 10 above — DONE.*
