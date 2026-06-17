# Elementor 3.21.1 — Design & Maintenance Reference
### Access Egypt Travel — accessegypttravel.com

> **Version note:** This guide covers Elementor Free + Pro features available in **3.21.1** (April 2024).
> Grid Container is active by default in this version. Flexbox Container is stable.

---

## Custom CSS Decision Rule

**Before writing any CSS, ask: does a UI control already do this?**

| What you want to do | Built-in control? | Write CSS? |
|---|---|---|
| Align items left/center/right inside a container | ✅ Flexbox → Justify Content | No |
| Stack items vertically vs side-by-side | ✅ Flexbox → Direction | No |
| Create a photo grid (2 col, 3 col, etc.) | ✅ Grid Container | No |
| Span an item across multiple grid cells | ✅ Grid → Cell Spanning | No |
| Change background color on hover | ✅ Container Style → Hover State | No |
| Add a box shadow on hover | ✅ Container Style → Hover State | No |
| Add a border on hover | ✅ Widget Style tab → Hover State | No |
| Fade element in as user scrolls | ✅ Motion Effects → Transparency | No |
| Scale element up on scroll | ✅ Motion Effects → Scale | No |
| Blur element on scroll | ✅ Motion Effects → Blur | No |
| Slide element into view on page load | ✅ Motion Effects → Entrance Animation | No |
| Parallax image on scroll | ✅ Motion Effects → Vertical Scroll | No |
| Make cursor tilt an element in 3D | ✅ Motion Effects → 3D Tilt | No |
| Apply image blur / brightness filter | ✅ Style → CSS Filters | No |
| Text outline / hollow text | ✅ Style → Text Stroke | No |
| Image/text blend with background | ✅ Style → Blend Mode | No |
| Gradient background | ✅ Style → Background → Gradient | No |
| Sticky header or sidebar | ✅ Advanced → Motion Effects → Sticky | No |
| Hide an element on mobile only | ✅ Advanced → Responsive → Hide on Device | No |
| Rounded corners | ✅ Style → Border Radius | No |
| Section shape divider | ✅ Style → Shape Divider (with custom units in 3.21) | No |
| Transparent-to-solid header on scroll | ❌ No built-in | **Yes — CSS needed** |
| Hover state on text color inside a widget | ❌ No built-in (widget-level) | **Yes — CSS needed** |
| CSS pseudo-elements (::before, ::after) | ❌ No built-in | **Yes — CSS needed** |
| nth-child or sibling selectors | ❌ No built-in | **Yes — CSS needed** |
| Force side-by-side columns on mobile (legacy sections) | ❌ No built-in for old sections | **Yes — CSS or switch to Flexbox Container** |

---

## 1. Core Architecture: Design System First

Always define globals before building anything. Changing a global updates every widget that uses it across the entire site instantly.

### Global Colors
**Access:** `Hamburger menu (☰) → Site Settings → Global Colors`

- Define: Primary, Secondary, Text, Accent, Background
- Apply: click the "Globe" icon in any color picker — it shows your globals instead of a hex field
- **Never hardcode a hex value if a global covers it.** If you change the global later, hardcoded values won't update.

### Global Fonts
**Access:** `Site Settings → Global Fonts`

- Define: Primary Heading, Secondary Heading, Body Text, Accent
- Apply: select from the "Globe" dropdown in any Typography control
- Set once, update everywhere

### Theme Style
**Access:** `Site Settings → Theme Style`

- Controls the default look of: buttons, headings (H1–H6), paragraphs, links, images, form fields
- Change here first — it sets the baseline so individual widgets inherit good defaults and need less per-widget styling

---

## 2. Layout: Flexbox Container (Stable in 3.21)

**Flexbox Container is the preferred layout system.** It replaces the old Section/Column structure and eliminates most manual flex CSS.

### What it replaces
- `display: flex`, `flex-direction`, `justify-content`, `align-items`, `flex-wrap`, `gap` — all available as UI controls

### Creating a Flexbox Container
`+ → Flex Container` in the editor (or convert an existing section)

### Key Controls (Layout tab)
| Control | What it does | Old CSS equivalent |
|---|---|---|
| **Direction** | Row (side-by-side) or Column (stacked) | `flex-direction` |
| **Wrap** | Whether items wrap to a new line when they overflow | `flex-wrap` |
| **Justify Content** | Spacing along the main axis (start, center, end, space-between, space-around, space-evenly) | `justify-content` |
| **Align Items** | Alignment on the cross axis (start, center, end, stretch) | `align-items` |
| **Gap** | Space between child elements (Row gap / Column gap) | `gap` |
| **Min Height** | Sets a minimum height for the container | `min-height` |

### Common Use Cases
- **Side-by-side two columns:** Direction = Row, Justify Content = Space Between
- **Centered content block:** Direction = Column, Justify Content = Center, Align Items = Center
- **Cards that wrap to new rows:** Direction = Row, Wrap = Wrap
- **Stacked mobile layout** (automatic): On mobile viewport, change Direction to Column

> **No custom CSS needed for mobile stacking.** Switch Direction to Column in the Mobile viewport tab.

---

## 3. Layout: Grid Container (Active by Default in 3.21)

Grid Container is **activated by default in 3.21** for all sites. It handles multi-column photo grids, tour card grids, and any equal-height card layout — no CSS needed.

### What it replaces
- `display: grid`, `grid-template-columns`, `grid-template-rows`, `grid-gap`, `grid-column: span X` — all UI controls

### Creating a Grid Container
`+ → Grid Container` in the editor

### Key Controls (Layout tab)
| Control | What it does | Old CSS equivalent |
|---|---|---|
| **Columns** | Number of columns (or set custom track sizes) | `grid-template-columns` |
| **Rows** | Number of rows (or Auto for content-driven) | `grid-template-rows` |
| **Column Gap** | Horizontal space between cells | `column-gap` |
| **Row Gap** | Vertical space between cells | `row-gap` |
| **Auto Rows** | Height of rows when row count is Auto | `grid-auto-rows` |

### Spanning Content Across Cells
Select a child widget → Layout tab → **Column Span** or **Row Span** → enter the number of cells to span.

Replaces: `grid-column: span 2` / `grid-row: span 2`

### Common Use Cases for This Site
- **Tour card grid** (3 cards per row): Columns = 3, Column Gap = 24px, Row Gap = 24px
- **Photo gallery** (masonry-style with spanning): mix of 1-cell and 2-cell span items
- **Destination overview tiles** (2 up): Columns = 2

---

## 4. Hover States (No CSS Needed)

In Elementor 3.21, Containers have built-in Hover state controls in the Style tab. This eliminates the most common reason to write custom `:hover` CSS.

### How to Access
1. Select a Container or Widget
2. Go to **Style tab**
3. At the top, toggle from **Normal** → **Hover**
4. Change: Background, Border, Box Shadow, Border Radius, Opacity, CSS Filter
5. Any value set in Hover state only applies when the user's cursor is over the element

### What this covers
- Card hover: background color change, border appears, shadow lifts
- Button hover: color shift, background change, border color change (for button widget, use Style tab → Button → Hover)
- Image hover: opacity change, CSS filter (grayscale → color, or blur → sharp)

### Hover Transition Speed
Style tab (Normal state) → **Transition Duration** — sets how fast the hover animation runs (in seconds, e.g., `0.3`)

### What still needs CSS
- Hover effects on **text color within a Text widget** (no built-in hover state for text color in 3.21)
- Hover effects that target a **child element** when a **parent** is hovered (CSS `:hover` selector chaining)

---

## 5. Motion Effects (Replaces AOS, GSAP, and Scroll JS)

**Access:** Any element → **Advanced tab → Motion Effects**

All of these work with zero custom CSS or JavaScript.

### Scrolling Effects
Triggered by the user's scroll position:

| Effect | What it does |
|---|---|
| **Vertical Scroll** | Element moves up or down as user scrolls (parallax) |
| **Horizontal Scroll** | Element drifts left or right during scroll |
| **Transparency** | Element fades in or out based on scroll depth |
| **Scale** | Element grows or shrinks as user scrolls |
| **Blur** | Element sharpens or blurs based on scroll depth |
| **Rotate** | Element spins during scroll |

Each effect has **Speed**, **Range** (which scroll range triggers it), and **Viewport** (when it starts relative to the viewport) controls.

### Mouse Effects
Triggered by cursor position:

| Effect | What it does |
|---|---|
| **3D Tilt** | Element tilts in 3D perspective toward the cursor |
| **Mouse Track** | Element moves slightly following cursor movement |

### Entrance Animations
**Access:** Advanced tab → Motion Effects → **Entrance Animation**

- Triggers once when the element scrolls into view
- Preset options: Fade In, Slide In (from any direction), Zoom In, Bounce In, Flip In, and more (~40 presets)
- Controls: **Duration** and **Delay** (in milliseconds)
- Replaces: AOS (Animate On Scroll) library, custom `@keyframes` + IntersectionObserver JS

---

## 6. Popup Builder

### Design Phase
Build popup layouts using any widget. The popup is designed like a page — drag, drop, style.

Special widgets useful in popups:
- **Text Path Widget:** Text follows a custom curved path — use for badge overlays ("Limited Time", "Private Tour Only")
- **Text Stroke:** Hollow/outlined heading text — Style tab → Typography → Text Stroke
- **Lottie Widget (Pro):** Play JSON animations inside popups — "Thank You" animations, loading states

### Triggers
| Trigger | When it fires |
|---|---|
| **On Click** | When a button or widget is clicked (via Dynamic Tags) |
| **On Page Load** | After X seconds |
| **Scroll** | When user reaches a % of page height |
| **Exit Intent** | When user's mouse moves toward the browser bar |
| **Inactivity** | After user is idle for X seconds |

### Conditions
Set which pages show the popup:
- Entire site, specific pages, post type, category, or tag
- Use conditions to avoid showing exit-intent popups on checkout or contact pages

### Wiring a Button to Open a Popup (Step-by-Step)
1. Build the popup in **Templates → Popups** — give it a clear name
2. Select the **Button widget** on your page
3. Content tab → **Link field** → click the Dynamic Tags icon (cylinder icon)
4. Under "Actions" → select **Popup**
5. Click "Popup" in the link field → set Action = "Open Popup" → select your popup by name
6. Publish and test

Same process works for a **Lottie widget** as the trigger — wire its Link field the same way.

### Popup Strategy for This Site
| Goal | Popup type |
|---|---|
| "Customize Your Trip" form | On Click → multi-step inquiry form |
| Email capture / lead magnet | Scroll trigger at 50% page depth |
| Exit offer ("Save $200") | Exit Intent — use sparingly, owner approval required |
| Tour itinerary PDF download | On Click → form + download confirmation |

---

## 7. Dynamic Tags

Dynamic Tags make buttons, images, and text pull live data — no custom PHP or JS needed.

### One-Click Communication (Most Useful for This Site)
- **WhatsApp Button:** Button widget → Link → Dynamic Tags → Contact URL → select WhatsApp → enter `+201201400578`
- **Phone Call:** Same process → select Tel → enter `+17727820494`
- **Email Link:** Contact URL → select Email → enter `info@accessegypttravel.com`

### Media and Content
- **Featured Image:** Map an image widget to a post's Featured Image tag — tour page templates update automatically when you change the post image
- **Dynamic Lightbox:** Images open in full-screen responsive overlay on click — no custom JS needed
- **Post Title / Excerpt / Date:** Populate text widgets from post data — essential for blog post templates

### Custom Fields (ACF or Pods)
If custom fields are installed (tour price, guide name, departure dates):
- Map any text/image widget to a custom field tag → Template auto-populates for every post
- Required for building a dynamic tour archive page that doesn't need manual updates

---

## 8. Theme Builder (Site-Wide Templates)

**Access:** `Templates → Theme Builder`

Build once, apply everywhere. Changes here cascade to all pages that match the condition.

| Template type | What it controls | Condition to use |
|---|---|---|
| **Header** | Top navigation, logo, phone/WA buttons | Entire site |
| **Footer** | Links, social icons, contact info, copyright | Entire site |
| **Single Post** | Blog/travel-tips article layout | All Posts |
| **Archive** | Tour category listing page grid | All Archives |
| **Single Page** | Default page layout | Any specific page |

### Sticky Header Setup
1. Design the header in Theme Builder
2. In the header section: **Advanced tab → Motion Effects → Sticky → Top**
3. To make it transparent at top and solid when scrolling, add CSS (see Section 9)

---

## 9. Custom CSS — When You Actually Need It

Only write CSS when the UI has no equivalent. All snippets go in **Advanced tab → Custom CSS** on the relevant element, or **Site Settings → Custom CSS** for global rules.

### Sticky Header: Transparent → Solid on Scroll
Add this to the header section's **Advanced → Custom CSS**:
```css
/* Header at top of page */
selector {
    background-color: transparent;
    transition: background-color 0.4s ease-in-out;
}

/* Header after user starts scrolling */
selector.elementor-sticky--effects {
    background-color: rgba(255, 255, 255, 0.95) !important;
    transition: background-color 0.4s ease-in-out;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}
```

### Force Columns Side-by-Side on Mobile (Legacy Sections Only)
Only needed if you're using the old Section/Column system. **If using Flexbox Container, change Direction to Row in Mobile viewport instead — no CSS needed.**
```css
@media (max-width: 767px) {
    selector .elementor-column {
        width: 50% !important;
        float: left;
    }
}
```

### Global Scripts (Custom Code Tool — Not CSS)
**Access:** `Site Settings → Custom Code`
Add to `<head>` or `<body>` globally — no theme file editing:
- WhatsApp chat widget (WATI, Tidio)
- Google Analytics 4 / GTM
- Facebook Pixel
- Hotjar / Microsoft Clarity (session recording)

---

## 10. Responsive Design

### The Right Approach per Layout System
| Layout | How to handle mobile |
|---|---|
| **Flexbox Container** | Change Direction to Column in Mobile viewport — no CSS |
| **Grid Container** | Change Columns to 1 in Mobile viewport — no CSS |
| **Old Section/Column** | Set Column Width to 50% in Mobile viewport, or use CSS |

### Responsive Mode
Bottom of editor panel → device icons → switch between Desktop, Tablet, Mobile.
**Changes made at Mobile do not affect Desktop.** This is device-specific, not cascading.

### Mobile-Only Elements
- Select any widget → **Advanced tab → Responsive → Hide on Device**
- Show "Call Now" sticky bar only on Mobile: build it, hide it on Desktop and Tablet

### Key Mobile Rules for This Site
- Hero sections: height = `100VH` (always fills screen, any device)
- Font sizes: use `VW` or `%` — never fixed `px` on headings
- CTA buttons ("Call" + "WhatsApp"): use a 2-column Flexbox Container, each child at 50% width
- Test at 375px width (iPhone SE) — if it holds there, it holds everywhere

---

## 11. Performance & Site Health

### Built-In Performance Features (3.21)
- **Improved Asset Loading** (merged stable in 3.21): Loads only the CSS/JS for widgets actually used on each page
- **Lazy Load Background Images** (Beta in 3.21): Background images in sections load only when scrolled into view — enable in **Settings → Elementor → Performance**
- **Image Optimization:** Compress before upload; Elementor has a built-in WebP converter in Pro

### Proactive Maintenance
- **Staging First:** Test significant changes in staging before pushing live. Most managed WP hosts (WP Engine, Kinsta, SiteGround) have one-click staging.
- **Maintenance Mode:** `Elementor → Tools → Maintenance Mode` — shows a "Coming Soon" page during major updates
- **Role Manager:** `Elementor → Role Manager` — restrict editor access to content-only; prevent non-designers from touching layouts
- **Element Manager** (available in 3.19+): `Elementor → Settings → Elements` — disable unused widgets for performance

### Accessibility
**Access:** Elementor Pro → `Ally by Elementor` tools
- Color contrast checker
- Line height controls
- Screen-reader friendly markup
- Required for inclusive design for all traveler types
