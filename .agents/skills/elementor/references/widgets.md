# Elementor 3.21 — Widget Reference
### Key settings and gotchas for the widgets used most on this site

---

## How to Find Any Widget
Left panel search bar → type partial name. If a widget is missing, check `WP Admin → Elementor → Settings → Elements` — it may be disabled in Element Manager.

---

## Text Widgets

### Heading Widget
- **HTML Tag:** Set to H1 on hero, H2 for section titles, H3 for card titles — never skip levels
- **Link:** Can make the entire heading a clickable link
- **Style → Typography → Text Stroke:** Creates hollow/outlined heading text — no CSS
- **Style → Typography → Text Shadow:** Subtle shadow on hero headings for legibility over images
- **Dynamic tag:** Wire to `Post Title` in blog/tour templates

### Text Editor Widget
- Full rich-text editor (bold, italic, lists, links)
- **Avoid for single lines** — use Heading widget instead (better SEO semantics)
- Hover color on inline text requires CSS (no built-in hover for text color)

### Icon List Widget
- Best for inclusions/exclusions lists on tour pages (✅ / ❌ with icons)
- Style → Space Between: controls gap between list items
- Each item: set its own icon, text, and link independently
- Use with Font Awesome or upload custom SVG icon set (`Site Settings → Custom Icons`)

---

## Image Widgets

### Image Widget
- **Style → Image Size:** Always set to the correct registered WordPress size — avoid "Full" for display images
- **Style → Object Fit:** `Cover` fills the container without distortion — use for consistent card thumbnails
- **Style → CSS Filters:** Grayscale, brightness, contrast — all hover-switchable (Normal vs Hover state)
- **Link → Lightbox:** Set to "Yes" for gallery images — opens full-screen overlay, no JS needed
- **Dynamic tag:** Wire to `Featured Image` in post templates

### Image Gallery Widget
- Grid display with built-in lightbox
- Style → Columns: set separately per device viewport
- Style → Gap: controls spacing between gallery images
- **Limitation:** Static list only — for dynamic gallery from posts, use Loop Builder instead

### Image Carousel Widget
- Auto-play, navigation arrows, dots — all configurable in Content tab
- Effect: Slide or Fade
- Style → Navigation → Arrows / Dots: color, size, position
- Works well for destination photo carousels and testimonial profile photos

---

## Button Widget

### Core Settings
- Content → Link: use Dynamic Tags for WhatsApp, Tel, Email, Popup — not hardcoded URLs
- Content → Icon: add an icon before or after the button text (Font Awesome or SVG)
- Style → Typography, Background Color, Border, Border Radius: set Normal and Hover states
- Style → Hover Animation: built-in hover animations (Grow, Shrink, Pulse, Bob, Wobble, etc.)

### Sizing
- Size presets: Extra Small / Small / Medium / Large / Extra Large
- **Custom size:** Advanced tab → Width → Custom → enter `%` or `px`
- For full-width button on mobile: set Width to 100% in Mobile viewport

---

## Form Widget (Pro)

### Field Types Available
Text, Email, Textarea, Number, Date, Time, Tel, Select, Checkbox, Radio, File Upload, Hidden, HTML, Step (for multi-step forms)

### Step Fields (Multi-Step Form)
- Add a "Step" field type to divide the form into pages
- Travelers see one step at a time — reduces intimidation for long inquiry forms
- Style each step's button in Style → Button

### Actions After Submit
`Content → Actions After Submit` — can chain multiple:
- **Email** — sends notification to `accessegypttravel@gmail.com`
- **Redirect** — send to a "Thank You" page after submission
- **Popup** — open a thank-you popup with a Lottie animation
- **Mailchimp / Kit / ActiveCampaign** — add to email list (requires plugin integration)

### Form Email Setup
Content → Actions → Email:
- **To:** `accessegypttravel@gmail.com`
- **Subject:** `New Tour Inquiry — [field id="name"]` (use field shortcodes)
- **Message:** Build with field shortcodes: `[field id="name"]`, `[field id="email"]`, etc.
- **From Email:** Use a `@accessegypttravel.com` address to avoid spam filters

### Anti-Spam
Content → Additional Options:
- **reCAPTCHA v3** (recommended — invisible, no checkbox)
- **Honeypot** field — invisible to humans, bots fill it in, form rejects automatically

---

## Navigation / Menu Widgets

### Nav Menu Widget (Pro)
- Displays any WordPress menu created in `Appearance → Menus`
- Style → Layout: Horizontal (desktop) / Dropdown (mobile)
- Style → Main Menu → Typography, Color, Hover Color: controls top-level items
- Style → Dropdown → controls the submenu panel

### Sticky Header Pattern (Theme Builder)
1. Build header in Theme Builder with Nav Menu + Logo + Button (WhatsApp/Call)
2. Header section → Advanced → Motion Effects → Sticky → Top
3. Sticky On: check Desktop, Tablet, Mobile
4. Offset: set to `0` unless another sticky bar exists above
5. Add transparent-to-solid CSS (see main SKILL.md snippets)

### Mobile Hamburger Menu
Nav Menu widget automatically collapses to hamburger at the Breakpoint set in:
`Site Settings → Layout → Breakpoints → Mobile Breakpoint`
Default: 767px. Change if design requires different breakpoint.

---

## Video Widget

### Basic Setup
- Content → Video Type: YouTube / Vimeo / Self Hosted / Dailymotion
- Content → Image Overlay: show a thumbnail image until user clicks to play — prevents auto-loading the video

### Background Video (on a Section/Container)
Section/Container → Style tab → Background Type → Video:
- Enter the video URL
- Start/End Time: trim which part plays
- Play Once: stop after first loop
- Play on Mobile: disable to save mobile data (show fallback image instead)
- **Always set a Fallback Image** — shown on mobile if video is disabled

### Performance Note
Background videos significantly increase page load. Only use on hero sections. Always set `Play on Mobile = No` and use a high-quality static image fallback.

---

## Testimonial & Review Widgets

### Testimonials Widget
- Supports image, quote, name, job title
- Style → Content / Name / Job: typography and color controls per element
- Use an Image Carousel widget for rotating testimonials

### Review / Star Rating Widget
For tour pages: display a star rating visually.
- Content → Rating: set the score (0–5, supports decimals like 4.7)
- Style → Color: change star color (use Global Accent color)

---

## Countdown Widget (Pro)
For time-sensitive offers ("Early Bird — 7 days left"):
- Content → Due Date: set the target date/time
- Actions After Expire: Hide, Show Message, or Redirect
- Style → Digits / Label: full typography control per section

---

## Loop Builder (Pro) — For Dynamic Tour Listings

### When to Use
When you need a page that automatically lists tour posts, blog posts, or any custom post type — without manually adding each card.

### How It Works
1. `Templates → Loop Item` → design a single card template using Dynamic Tags (Post Title, Featured Image, Excerpt, Custom Fields)
2. `Add a Loop Grid widget` to your page
3. Point it at the template you designed
4. Set `Post Type`, `Filter by Taxonomy`, `Posts Per Page`
5. The grid auto-populates from your WordPress posts — add a new post, it appears automatically

### Loop Grid Controls
- Columns: set per device viewport
- Gap: row and column spacing
- Filters: show only posts in a specific category (e.g., only "Nile Cruise" tours)
- Pagination: number / Load More button / Infinite Scroll

### Why This Matters for This Site
Without Loop Builder, every tour card on a listing page must be manually updated when a tour changes. With Loop Builder, update the WordPress post → all listing pages update automatically.

---

## Global Widgets (Pro)

### What They Are
A widget (or group of widgets in a Container) saved globally — edit it once, updates everywhere it appears.

### Best Use Cases for This Site
- WhatsApp/Call button pair — appears in header, footer, and mobile CTA bar
- "Book Now" CTA block — same design appears on every tour page
- Social media icon row — footer + about page

### How to Create
Right-click any widget → `Save as Global` → name it clearly.

### How to Edit
Edit it on any page where it appears → the change propagates to all instances automatically.

### Limitation
Global Widgets are locked — you can only edit them through the "Edit Global" option, not by directly editing the instance. This prevents accidental per-page changes.

---

## Flip Box Widget

### What It Is
A card with a "front" face and a "back" face. The back reveals on hover with a flip animation.

### Best Use Cases for This Site
- Tour highlight cards: front = destination photo + name, back = key detail + "Explore" button
- "Why Us" cards: front = icon + title, back = explanation paragraph
- Team cards: front = photo, back = short bio

### Setup
Content tab:
- Front: choose Icon or Image, Title, Description
- Back: Title, Description, Button (label + link)

Style tab → Box → **Flip Effect**: Classic, 3D, Fade, Zoom In/Out, Slide

### Height
Style → Box → Height: set a fixed height (e.g., `300px`) — both front and back must be the same height.

---

## Accordion & Toggle Widgets

### Nested Accordion (Pro, stable in 3.18)
- Use for FAQs on tour pages — keyboard accessible, ARIA-compliant
- Supports nested levels (accordion within accordion)
- Style → Header / Content: full typography and color control
- Set `Default Active Item` to open the first FAQ by default

### Toggle Widget
Same as Accordion but items don't auto-close when another opens. Use when users may want multiple sections open simultaneously.

---

## Shortcode Widget
Renders any WordPress shortcode inside an Elementor layout.
Use cases:
- Contact Form 7 forms (if switching from Elementor Forms)
- Booking calendar plugins
- Payment buttons

---

## HTML Widget
Embeds raw HTML directly. Use for:
- Embedded maps (Google Maps iframe)
- Third-party booking widgets
- Custom HTML elements not available as widgets

**Security:** Only paste HTML from trusted sources. Never paste user-submitted content.

---

## Shape Divider (Section/Container)
Not a widget — it's a section style setting.
`Section → Style → Shape Divider → Top or Bottom`

Types: Triangle, Tilt, Curve, Zigzag, Arrow, Book, Mountains, Clouds, Drops, and more.
- **Width %:** stretch or compress the shape
- **Height (px):** control how tall the divider is
- **Flip:** mirror the shape horizontally
- **Invert:** swap foreground/background fill direction
- **Color:** must match the adjacent section's background color to create a seamless transition

In 3.21: shape divider supports custom units for width and height (not just px).

---

## Spacer & Divider Widgets

### Spacer Widget
Adds vertical whitespace. In Flexbox/Grid layouts, use **Gap** on the container instead — more consistent and responsive. Spacer is a fallback for legacy layouts.

### Divider Widget
Horizontal rule between sections. Style → Color, Weight (thickness), Gap (space above/below). Can add an icon centered on the divider line.
