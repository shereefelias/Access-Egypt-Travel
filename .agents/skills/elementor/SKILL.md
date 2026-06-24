---
name: elementor
description: Complete Elementor 3.21.1 guide for accessegypttravel.com. Use when asked to build a page, edit a layout, add a popup, configure hover effects, fix mobile display, wire a button to a popup, add a sticky header, insert custom CSS, set up Dynamic Tags, configure a WhatsApp button, create a tour card grid, add scroll animations, or do anything involving the Elementor editor on this WordPress site. Covers Flexbox Container, Grid Container, Motion Effects, Popup Builder, Theme Builder, Dynamic Tags, and the custom CSS decision rule.
---

## Site Context

- **URL:** accessegypttravel.com
- **Stack:** WordPress + Elementor Pro 3.21.1
- **Layout system:** Flexbox Container (stable) + Grid Container (active by default in 3.21)
- **Do NOT use old Section/Column layout for new pages** — use Containers
- **WordPress MCP (Vibe AI):** Available for direct publish/edit

### Reference Files (read when working on specific areas)
| Topic | File |
|---|---|
| Full CSS decision rules, layout, hover, motion, popups, dynamic tags | `wd_elemntor.md` (project root) |
| All 40+ widgets — settings, gotchas, use cases | `references/widgets.md` |
| Navigator, shortcuts, copy/paste, templates, revision history | `references/editor-workflow.md` |
| Section recipes for hero, tour cards, FAQs, CTAs, blog templates | `references/design-patterns.md` |

---

## The #1 Rule: Check UI Before Writing CSS

Most CSS developers reach for custom code out of habit. In Elementor 3.21, most layout and style needs are covered by built-in controls. Write CSS only when the table below says "Yes."

| Task | Built-in? | Write CSS? |
|---|---|---|
| Flex direction, wrap, justify, align, gap | ✅ Flexbox Container Layout tab | No |
| Multi-column card grid | ✅ Grid Container | No |
| Span grid cell across multiple columns | ✅ Grid → Cell Span | No |
| Background / border / shadow on hover | ✅ Style tab → Hover state | No |
| Image opacity / filter on hover | ✅ Style tab → Hover state → CSS Filter | No |
| Scroll-based parallax / fade / scale | ✅ Advanced → Motion Effects → Scrolling | No |
| Entrance animation on scroll into view | ✅ Advanced → Motion Effects → Entrance Animation | No |
| 3D tilt or mouse-track effect | ✅ Advanced → Motion Effects → Mouse Effects | No |
| Sticky header or sticky sidebar | ✅ Advanced → Motion Effects → Sticky | No |
| Hide element on mobile/tablet/desktop | ✅ Advanced → Responsive → Hide on Device | No |
| Rounded corners | ✅ Style → Border Radius | No |
| Box shadow or text shadow | ✅ Style → Shadow controls | No |
| Gradient background | ✅ Style → Background → Gradient | No |
| Image blend mode | ✅ Style → Blend Mode | No |
| CSS filters (blur, brightness, contrast) | ✅ Style → CSS Filters | No |
| Hollow / outlined text | ✅ Style → Typography → Text Stroke | No |
| Section shape divider | ✅ Style → Shape Divider | No |
| Responsive font size per device | ✅ Change value in Mobile viewport mode | No |
| Column width per device | ✅ Set Column Width in Mobile viewport mode | No |
| Absolute or fixed element positioning | ✅ Advanced → Positioning → Absolute/Fixed | No |
| Z-index stacking order | ✅ Advanced → Positioning → Z-Index | No |
| Transparent-to-solid sticky header | ❌ No built-in | **CSS — see snippet below** |
| Hover color change on inline text | ❌ No built-in | **CSS — use Custom CSS tab** |
| Style a child element when its parent is hovered | ❌ No built-in | **CSS — `.parent:hover .child {}` in Custom CSS** |
| ::before / ::after pseudo-elements | ❌ No built-in | **CSS — use Custom CSS tab** |
| nth-child / sibling CSS selectors | ❌ No built-in | **CSS — use Custom CSS tab** |
| Side-by-side columns on mobile (old sections only) | ❌ Only for legacy sections | **CSS or switch to Flexbox Container** |

---

## Global Design System (Do This First)

Every page inherits from these. Set them before building anything.

### Global Colors
`☰ → Site Settings → Global Colors`
- Define: Primary, Secondary, Text, Accent, Background
- Apply via the **Globe icon** in any color picker
- Never hardcode a hex if a global covers it

### Global Fonts
`☰ → Site Settings → Global Fonts`
- Define: Primary Heading, Secondary Heading, Body, Accent
- Apply via the Globe dropdown in any Typography control

### Theme Style
`☰ → Site Settings → Theme Style`
- Sets defaults for: H1–H6, paragraphs, links, buttons, form fields
- Always configure this first — widgets inherit these defaults and need less per-widget styling

---

## Flexbox Container (Primary Layout Tool)

**Use for:** rows of cards, hero sections, nav bars, feature sections, any side-by-side or stacked layout.

### How to Create
`+ button in editor → Flex Container`

### Layout Tab Controls
| Control | What it does | Old CSS |
|---|---|---|
| Direction | Row = side-by-side / Column = stacked | `flex-direction` |
| Wrap | Items wrap to next row when full | `flex-wrap: wrap` |
| Justify Content | Spacing on main axis (start/center/end/space-between/space-around/space-evenly) | `justify-content` |
| Align Items | Alignment on cross axis (start/center/end/stretch) | `align-items` |
| Gap (Row + Column) | Space between items | `gap` |
| Min Height | Minimum height | `min-height` |

### Responsive Behavior (No CSS Needed)
- Desktop: Direction = Row → side-by-side
- Mobile viewport: change Direction = Column → stacked
- No custom CSS. No media queries.

### Common Patterns for This Site
- **Two-card row:** Direction = Row, Justify = Space Between, Gap = 24px
- **Centered hero content:** Direction = Column, Justify = Center, Align Items = Center
- **Call + WhatsApp buttons side-by-side on mobile:** Flexbox Container, Direction = Row, each button = 50% width (set in the button's Width control in Advanced tab → set to Custom → 50%)
- **Feature list (icon + text):** Direction = Row, Align Items = Center, Gap = 12px

---

## Grid Container (Active by Default in 3.21)

**Use for:** tour card grids, photo galleries, destination tile layouts — any equal-column grid.

### How to Create
`+ button in editor → Grid Container`

### Layout Tab Controls
| Control | What it does | Old CSS |
|---|---|---|
| Columns | Number of columns (or custom track sizes like `1fr 2fr 1fr`) | `grid-template-columns` |
| Rows | Number of rows, or Auto | `grid-template-rows` |
| Column Gap | Horizontal space between cells | `column-gap` |
| Row Gap | Vertical space between cells | `row-gap` |
| Auto Rows | Height of auto-generated rows | `grid-auto-rows` |

### Cell Spanning
Select a **child widget** inside the grid → Layout tab → **Column Span** or **Row Span** → enter number of cells.
- Replaces: `grid-column: span 2`

### Responsive: Reduce Columns on Mobile
- Mobile viewport → change Columns from `3` to `1` → no CSS

### Common Patterns for This Site
- **Tour cards (3 per row):** Columns = 3, Column Gap = 24px, Row Gap = 32px
- **Photo gallery (featured large + smaller):** Columns = 3, first item Column Span = 2
- **Destination tiles (2 up):** Columns = 2, auto rows with equal height
- **Why Us features (4 icons):** Columns = 4 → Columns = 2 on Tablet → Columns = 1 on Mobile

---

## Hover States (Style Tab)

**Access:** Select element → **Style tab → toggle Normal → Hover** at the top of the tab.

### What You Can Change on Hover
- Background color / image / gradient
- Border color, width, radius
- Box shadow
- Opacity
- CSS Filters (blur, brightness, contrast, grayscale, saturate)
- Text color (on button widgets — button Style tab → Hover)

### Setting Hover Transition Speed
In **Normal state** → Style tab → scroll down to **Transition Duration** → enter value in seconds (e.g., `0.3`).
This controls how smoothly the element transitions between Normal and Hover states.

### Patterns for This Site
- **Tour card hover:** Container → Style tab → Hover → change background to slightly lighter sand, add box shadow `0 8px 24px rgba(0,0,0,0.12)`, Transition = 0.25s
- **Button hover:** Button widget → Style → Hover → Background = deeper color, no border
- **Team photo hover:** Image widget → Style → Hover → CSS Filter → Brightness 110%

### What Still Needs CSS (Hover Edge Cases)
- **Text color hover inside a Text widget** — no built-in hover state for text color in 3.21; use `.elementor-widget-text-editor:hover p { color: #xxx; }` in Custom CSS
- **Style a child when parent is hovered** — no UI for parent→child hover chaining; use `.parent-css-class:hover .child-css-class {}` in the parent container's Custom CSS tab

---

## Motion Effects (Replaces AOS, GSAP, scroll JS)

**Access:** Any element → **Advanced tab → Motion Effects**

### Scrolling Effects
All triggered by the user's scroll position. Settings: Speed, Affects (element or viewport), Range.

| Effect | Use case for this site |
|---|---|
| Vertical Scroll | Hero image drifts up as user scrolls (parallax) |
| Transparency | Section fades in as it enters viewport |
| Scale | Image zooms subtly during scroll |
| Blur | Image sharpens as it comes into view |
| Horizontal Scroll | Text or icons slide in from the side |
| Rotate | Decorative element spins during scroll |

### Entrance Animations
**Advanced → Motion Effects → Entrance Animation**
- Fires once when element enters the viewport
- ~40 presets: Fade In, Slide In from Bottom/Left/Right, Zoom In, Bounce In, Flip In
- Set **Duration** (ms) and **Delay** (ms) to stagger multiple elements
- **Staggering tip:** Give multiple elements the same animation but different delays (0ms, 100ms, 200ms) to cascade them in

### Mouse Effects
| Effect | Use case |
|---|---|
| 3D Tilt | Tour card tilts toward cursor — strong for hero CTAs |
| Mouse Track | Element follows cursor slightly — hero background image |

---

## Popup Builder

### Creating a Popup
`Templates → Popups → Add New`

Design the popup like any Elementor page. Use any widget. Pro widgets available: Lottie, Form, Countdown.

### Trigger Types
| Trigger | How to use |
|---|---|
| On Click | Wire to a button via Dynamic Tags (see below) |
| Page Load | Set delay in seconds |
| Scroll | Set % of page scroll depth |
| Exit Intent | Mouse leaves viewport toward browser bar |
| Inactivity | User idle for X seconds |

### Conditions
Set in Popup settings → Conditions tab. Restrict which pages show this popup:
- Entire Site / Front Page / Specific page / Post type / Category
- **Always restrict Exit Intent popups** — don't show them site-wide without the owner's sign-off

### Wiring a Button to Open a Popup
1. Create popup in `Templates → Popups`, name it clearly
2. Select the Button widget on your page
3. Content tab → **Link field** → click the Dynamic Tags icon (cylinder icon)
4. Under "Actions" → choose **Popup**
5. Click "Popup" in the Link field → Action = "Open Popup" → pick your popup by name
6. Publish and test on mobile too

Same steps work for Lottie widget as the trigger.

### Popup Strategy for This Site
| Goal | Trigger | Notes |
|---|---|---|
| "Customize Your Trip" form | On Click | Wire to "Start Now" button — include multi-step form |
| Email capture | Scroll at 60% | Offer a free Egypt packing guide PDF |
| Exit offer | Exit Intent | "Before you go — save $200" — owner approval required |
| Itinerary PDF | On Click | Form + download link on submit |

---

## Dynamic Tags

Dynamic Tags wire Elementor widgets to live data — no PHP, no JavaScript.

### WhatsApp & Phone Buttons (Most Important for This Site)
1. Add a Button widget
2. Content tab → Link field → Dynamic Tags icon
3. Choose **Contact URL**
4. Type = **WhatsApp** → Number = `+201201400578` (Egypt) or **Tel** → `+17727820494` (US)
5. Optional: pre-fill a message like `"Hi, I'd like to ask about a tour"`

### Email Link
Same process → Type = **Email** → `info@accessegypttravel.com`

### Post Data (For Blog / Tour Templates)
In a Single Post Template in Theme Builder:
- **Post Title** → Heading widget → Dynamic Tags → Post Title
- **Featured Image** → Image widget → Dynamic Tags → Featured Image
- **Post Excerpt** → Text Editor → Dynamic Tags → Post Excerpt
- **Author Name / Bio** → Text widget → Author

Templates built this way update automatically for every post — no manual content entry.

### Custom Fields (ACF or Pods — If Installed)
Map to any widget:
- Tour price → Text/Heading widget → Dynamic Tags → ACF → select field
- Guide name, departure dates, group size limits → same process
- Enables a real dynamic tour archive that never needs manual updates

---

## Theme Builder

`Templates → Theme Builder`

### What to Build Here
| Template | Condition | Purpose |
|---|---|---|
| Header | Entire Site | Navigation, logo, WhatsApp/Call buttons |
| Footer | Entire Site | Links, social icons, copyright, contact |
| Single Post | Post Type: Post | Blog article layout |
| Single Page | Page (if custom layout needed) | Specific page design |
| Archive | Archive: Post Category | Tour category listing grid |

### Sticky Header Setup
1. Design header in Theme Builder
2. Select the header section → **Advanced tab → Motion Effects → Sticky → Top**
3. Set **Sticky On** = Desktop + Tablet + Mobile
4. For transparent-to-solid effect: add Custom CSS (snippet below)

---

## Required Custom CSS Snippets

Only two situations require custom CSS in most standard builds.

### 1. Sticky Header: Transparent → Solid on Scroll
Add to the header section's **Advanced → Custom CSS:**
```css
/* Transparent at top */
selector {
    background-color: transparent;
    transition: background-color 0.4s ease-in-out;
}

/* Solid when scrolling — Elementor adds this class automatically */
selector.elementor-sticky--effects {
    background-color: rgba(255, 255, 255, 0.95) !important;
    transition: background-color 0.4s ease-in-out;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}
```

### 2. Force Side-by-Side Columns (Legacy Section Only)
Only needed if the page still uses the old Section/Column system.
**Better solution: convert to Flexbox Container.**
```css
@media (max-width: 767px) {
    selector .elementor-column {
        width: 50% !important;
        float: left;
    }
}
```

### 3. Global Scripts (Custom Code Tool — not CSS)
`☰ → Site Settings → Custom Code`
Add to `<head>` or `<body>` globally:
- WhatsApp chat widget (WATI, Tidio)
- Google Analytics 4 / GTM tag
- Facebook Pixel
- Session recording (Hotjar, Clarity)

---

## Mobile / Responsive Rules

### Responsive Approach by Layout System
| Layout system | How to handle mobile — no CSS needed |
|---|---|
| **Flexbox Container** | Mobile viewport → Direction = Column → items stack |
| **Grid Container** | Mobile viewport → Columns = 1 → single column |
| **Old Section/Column** | Set Column Width to 50% in Mobile viewport, or use CSS — better to convert to Container |

### Per-Device Editing
Bottom toolbar → device icons → Desktop / Tablet / Mobile.
Changes in Mobile view do not affect Desktop. This is device-specific.

### Standard Mobile Rules for This Site
- Hero height: `100VH` — never a fixed pixel value
- Heading sizes: set in Mobile viewport to avoid text overflow
- Flexbox hero: Direction = Column in Mobile viewport
- Grid tour cards: Columns = 1 in Mobile viewport
- Call + WhatsApp CTAs: Flexbox Container, Direction = Row, each button at 50% — no CSS
- Test at 375px (iPhone SE) — the tightest common phone

### Hiding Elements Per Device
Element → **Advanced → Responsive → Hide on Device**
- Show a mobile sticky CTA bar only on Mobile (hide on Desktop + Tablet)
- Hide heavy parallax sections on Mobile (show a simple image instead)

---

## Performance (Built Into 3.21)

### Enable These in Settings
`WP Admin → Elementor → Settings → Performance`
- ✅ **Improved Asset Loading** (merged stable in 3.21) — loads only CSS/JS for widgets on that page
- ✅ **Lazy Load Background Images** (Beta in 3.21) — section backgrounds load on scroll
- ✅ **Optimized Gutenberg Loading** — skips Gutenberg assets when Elementor is active

### Element Manager (3.19+)
`WP Admin → Elementor → Settings → Elements`
Disable widgets you're not using (WooCommerce, Countdown, etc.) — reduces CSS/JS loaded on every page.

---

## Accessibility

**Elementor Pro → Ally tools**
- Contrast checker — run before publishing any page
- Line height controls — minimum 1.5 for body text
- Screen reader compatibility — use proper heading hierarchy (H1 → H2 → H3, no skipping)
- Nested Accordion widget (introduced 3.18) is keyboard-accessible and ARIA-compliant — use it instead of custom accordion code

---

## WordPress MCP (Vibe AI) Integration

When using the WordPress MCP for this site:
- Start every task with `load_skill` query
- Use `rest_api` for content edits and post creation
- Use `upload_media` to upload images (NOT `rest_api` — it cannot upload files)
- **Build in draft first.** Only call `publish_draft_theme` when owner explicitly says "publish", "go live", or "ship it"
- Before any destructive WP-CLI command: confirm owner has a recent backup (check for UpdraftPlus, Solid Backups, or host-level backup)

---

## Editor Workflow Essentials

- **Navigator** (`Ctrl/Cmd + I`): element tree — use it to find buried widgets and rename containers
- **Right-click → Paste Style**: copies look from one widget to another without touching content
- **Right-click → Save as Template**: save any section/container to the library for reuse across pages
- **Right-click → Copy & Paste Cross-Site**: transfer elements between WordPress sites
- **Revision History** (clock icon, bottom bar): restore to any prior save point
- **Global Widgets**: right-click → Save as Global — edit once, updates everywhere (WhatsApp button, Book Now CTA)
- **Notes** (speech bubble, bottom bar, new in 3.21): leave team notes on elements — visible in editor only
- **Page Settings** (gear icon): always set "Hide Title = Yes" on Elementor-built pages
- Full workflow details: `references/editor-workflow.md`

---

## Common Widget Quick-Reference

| Need | Widget | Key setting |
|---|---|---|
| Multi-item FAQ | Nested Accordion (Pro) | Default Active = first item; ARIA-compliant |
| Rotating testimonials | Image Carousel | Auto-play + Dots navigation |
| Tour inclusions list | Icon List | Green check icon per item |
| Star review display | Star Rating | Rating field + accent color |
| Multi-step inquiry form | Form (Pro) | Add "Step" field type between sections |
| Video background on hero | Section → Style → Background → Video | Always set Play on Mobile = No |
| Dynamic tour listing | Loop Builder (Pro) | Loop Item template + Loop Grid widget |
| Hover card (front/back) | Flip Box | Set fixed height on Style → Box |
| Full-width inline map | HTML Widget | Paste Google Maps iframe |
| Inline countdown | Countdown (Pro) | Actions After Expire = Redirect or Message |

Full widget docs: `references/widgets.md`

---

## What NOT to Do

- Don't use old Section/Column for new pages — use Flexbox or Grid Container
- Don't hardcode hex colors — use Global Colors
- Don't write `display: flex` or `grid-template-columns` CSS — use the container controls
- Don't install AOS or jQuery scroll animation plugins — Motion Effects handles it
- Don't add Exit Intent popups without owner approval
- Don't publish live without owner review (draft → preview → owner says yes → publish)
- Don't use fixed `px` for font sizes or section heights on mobile viewports
- Don't skip testing at Mobile viewport before marking any page task complete
- Don't leave the WordPress page title visible on Elementor pages — always `Page Settings → Hide Title = Yes`
- Don't use Spacer widgets inside Flex/Grid containers — use Container Gap instead
- Don't add custom CSS in `Site Settings → Custom CSS` for element-specific styles — use the element's own `Advanced → Custom CSS` tab to avoid specificity conflicts
