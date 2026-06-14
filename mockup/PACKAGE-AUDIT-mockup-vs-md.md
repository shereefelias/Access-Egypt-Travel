# Package Audit — pages-mockup.html vs. source .md files

Date: 2026-06-14
Purpose: Flag every difference between the source package markdown and what was actually built into `pages-mockup.html`. Nothing here is "fixed" — these are items for your manual review/decision.

Legend:
- 🔴 **Decision needed** — factual conflict (price, nights, routing) or invented fact not in source
- 🟠 **Added content** — appears in mockup, not in source md at all
- 🟡 **Minor** — wording/detail drift, low risk

Source files cross-checked:
- `6_Days_Cairo_Luxor_v2.md` (used for the 6-day page) and the older `6 days 5 nights by air.md` (superseded)
- `7 Days , 6 nights.md`
- `8 days , 7 nights.md`
- `9days -  8 nights.md`
- `11 days. 10 nights.md`

---

## 0. Source files that contradict themselves (root cause of most flags)

The mockup couldn't have matched these because the source disagrees internally. The builder picked one value:

| Package | Conflict inside the source md | Value mockup used |
|---|---|---|
| 6-day | Tagline "From **$1,900**" vs. pricing table "From **$1,950**" | $1,950 ✅ RESOLVED — owner confirms **$1,950 is correct**; mockup already matches. (The two 6-day .md files are the same package.) |
| 7-day | Title "6 nights" but nights add to **5** (2 Cairo + 2 Luxor + 1 Aswan); plus leftover "Day 7 / Day 8" rows | rebuilt to 6 nights by adding a Luxor night (see 7-day below) |
| 9-day | Glance says "Cairo **4 nights**" but Inclusions + Accommodation say "Cairo **3 nights**" | 3 nights |
| 11-day | Glance "Nile Cruise **7 nights**" vs. Inclusions "cruise **4 nights**"; pricing table "From **$3,250**" vs. headline "**$3,950**"; itinerary incomplete | cruise 4 nights / $3,950 |

You should decide the correct figure for each, then I'll make source + mockup agree.

---

## 1. 6 Days / 5 Nights — Cairo & Luxor

🔴 **Valley of the Kings tomb names are invented.** Source says "3 standard tombs **plus Ramesses VI tomb**." Mockup Day 5 says "tombs of **Ramesses II, Tutankhamun, and others**." Tutankhamun and Ramesses II are *not* in your source and Tut's tomb carries a separate ticket. Verify what's actually included.

🟠 **Entire Accommodation section was added.** The 6-day source has **no accommodation section**. The mockup added Standard (Steigenberger Pyramids / Steigenberger Nile Palace) and Premium (Four Seasons / Marriott Mena House / Sofitel Winter Palace) — borrowed from the 9/11-day templates. Confirm these hotels apply to this package.

🟠 **Overview rewritten + "22 years" guide claim added.** Source intro was a placeholder marked "(Pls rephrase)." Mockup wrote a new intro and added "a guide who's spent **22 years**…" — that figure comes from the 9-day source, not this one.

🟡 Abu Simbel optional add-on: source listed it but you wrote "(this should be removed)." Mockup **did remove it** — confirming it's intentionally gone.

🟡 "Luxor Temple … **lit up at night/sunset**" added to highlights and Day 4; source for this package didn't say "lit up."

🟡 Accommodation intro says "**4–5 star**" while source inclusions say "5-star."

🟡 Open question from your source not addressed: "We should include how many meals in total." Mockup still only says "Breakfast + Lunch (Days 1–5)" — no total count.

---

## 2. 7 Days / 6 Nights — Cairo, Luxor & Aswan

🔴 **Luxor nights changed 2 → 3.** Source inclusions say "**2 nights** Luxor"; mockup glance + accommodation say "**3 nights** Luxor." The builder added a Luxor night so the total reaches 6 nights (source only added to 5). Decide the real allocation.

🔴 **Itinerary restructured; an overnight dropped.** Source had leftover Day 7 (Aswan tour) **and** Day 8 (final departure) with a Cairo airport-hotel overnight. Mockup compressed this into a single Day 7 where you fly Aswan→Cairo→international **same day**, removing the implied extra Cairo night. Confirm whether travelers overnight in Cairo before flying home.

🟡 Nubian Village: source lists it as an **included Aswan site**; mockup Day 7 calls it an "**optional** Nubian Village visit." Downgrade — confirm intent.

🟡 VoK text says "Ramesses **V & VI**"; this package's source said "Ramesses VI" only (the V & VI phrasing comes from the 8/9-day sources).

🟠 Aswan hotels added (Sofitel Legend Old Cataract / Mövenpick / Basma) — no accommodation section in source.

✅ Group 4–7 line correctly kept your "**10% discount — Exclusive Offer**" wording here (other pages say "10% discount applied").

---

## 3. 8 Days / 7 Nights — Cairo, Aswan & Nile Cruise

🔴 **Return-flight routing is wrong in Inclusions.** Mockup inclusions say "Domestic flight **Cairo → Aswan and return**." But the itinerary flies **Cairo → Aswan** (Day 3) and returns **Luxor → Cairo** (Day 7) — the return is from **Luxor, not Aswan**. Fix the wording.

🟡 **VoK tomb detail dropped.** Source Day text: "3 tombs plus Ramesses 5th & 6th." Mockup Day 7 just says "Valley of the Kings" with no tomb count.

🟠 Accommodation section added (Aswan: Sofitel Legend Old Cataract; cruise ships named) — source has no accommodation section.

🟡 Itinerary cleanup: source had a **duplicate "Day 6"** and stopped at Day 7. Mockup correctly renumbered to Day 6 + Day 7 + Day 8. (Improvement, but verify the split reads right.)

🟡 "Unfinished Obelisk" appears in the itinerary but not in the Highlights list (this matches the source's own omission — noting in case you want it added to Highlights).

---

## 4. 9 Days / 8 Nights — Pyramids, Luxor & Nile Cruise

🔴 **Cairo nights: source says both 4 and 3.** Glance said "Cairo (4 nights)"; mockup used "Cairo (3 nights)" (matching the source's Inclusions/Accommodation). Confirm 3 is correct.

🟡 **Colossi of Memnon dropped from Day 5 text.** Source Day 5 includes Colossi; mockup Day 5 narrative lists only VoK, Hatshepsut, Deir el-Medina. (Colossi is still in the Highlights list.)

🟡 VoK tomb detail ("3 royal tombs plus Ramesses 5th & 6th") not carried into mockup Day 5 narrative.

🟡 Inclusions flight line generalized: source "Domestic flights **Cairo → Luxor and Aswan → Cairo**"; mockup list just says "Domestic flights included."

🟡 Hotel spelling: source "Marriott **Mina** House"; mockup "Marriott **Mena** House." (Mena is the real-world spelling — flagging only so you pick one consistently.)

✅ Meals fixed: source had stray "(Days 1–5)"; mockup correctly shows "Cairo & Luxor: Breakfast + Lunch / Cruise: all meals."

---

## 5. 11 Days / 10 Nights — Ultimate Egyptian Odyssey

🔴 **Cruise length is unresolved and internally inconsistent.** Source glance said cruise "**7 nights**"; source inclusions said "**4 nights**" (copied from the 9-day). Mockup glance says "Nile Cruise (4 nights)" — **but the mockup's own itinerary puts travelers on the cruise Days 4–8 = 5 nights.** Glance (4) ≠ itinerary (5) ≠ source (7). This needs a definitive answer.

🔴 **Two itinerary days were invented to fill the trip.** The source day-by-day was incomplete (it ended around a duplicated "Day 9"). To reach 11 days the mockup added **Day 8 "Free Day (Abu Simbel optional)"** and **Day 10 "Optional Cairo Bonus Day."** These are not in any source — confirm they're real inclusions, not filler.

🔴 **Specific tombs invented in Day 5.** Mockup claims "**4 royal tombs including Ramesses II, Ramesses IV, Ramesses VI, and Seti I**," plus "Queen **Nefertari** … world-famous painted ceiling." Source Day 5 text only said "3 royal tombs plus Ramesses 5th & 6th." The named tombs (Ramesses II, IV, Seti I, Nefertari) are not in source; Nefertari and Seti I are premium-ticket tombs. Verify before publishing.

🔴 **Pricing source conflict.** Source pricing table said "From **$3,250**" (copied from 9-day); headline said "$3,950." Mockup used $3,950 throughout. Confirm.

✅ Highlights correctly added Madinet Habu, Valley of the Queens, Nobles' Tombs, and the Dendera optional add-on (all present in source).

✅ Meals + cruise-meal lines fixed from the source's stray "(Days 1–5)."

---

## 6. Applies to ALL five pages (added, not from any package md)

🟠 **Reviews block** (Tripadvisor "4.9 · 71 reviews · #137 of 1,289 Tours in Luxor" + four review titles) is on every page. Not from the package md files — verify the rating, review count, and ranking are current/accurate before publishing.

🟠 **"Your Route" map** section added on each page (you did ask for a map — flagging that it's placeholder).

🟡 Note on the 6-day: the older `6 days 5 nights by air.md` describes a **night train to Luxor** and lists nights differently. The mockup correctly used the newer `6_Days_Cairo_Luxor_v2.md` (domestic flights). The old file looks superseded — consider deleting it to avoid confusion.

---

## Suggested order of decisions
1. Lock the **night allocation** for 7-day (Luxor 2 vs 3), 9-day (Cairo 3 vs 4), 11-day (cruise nights + the two invented days).
2. Lock the **prices** where the source conflicts (6-day $1,900/$1,950; 11-day $3,250/$3,950).
3. Decide **which tombs** are genuinely included (6-day and 11-day both have invented names; Tut/Nefertari/Seti I are extra-ticket).
4. Fix the **8-day return-flight wording** (Luxor→Cairo, not Aswan→Cairo).
5. Confirm the **added accommodation sections** (6, 7, 8-day) and the **Reviews block** numbers.
