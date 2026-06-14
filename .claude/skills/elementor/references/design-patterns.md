# Elementor 3.21 — Design Patterns for Access Egypt Travel
### Reusable page section recipes specific to this site

---

## Hero Section

### Structure
```
Flexbox Container (Full Width, Min Height = 100VH)
  └── Background: full-cover image + dark overlay
  └── Inner Container (Boxed, Direction = Column, Justify = Center, Align = Center)
      ├── Heading (H1) — tour or page title
      ├── Text Editor — 1-sentence hook
      └── Flexbox Container (Direction = Row, Gap = 16px)
          ├── Button — "Book This Tour" (Primary style, links to inquiry form)
          └── Button — "WhatsApp Us" (Outlined style, Dynamic Tags → WhatsApp)
```

### Settings
- Outer container: Background Type = Classic → Image → Size = Cover, Position = Center
- Background Overlay: Style → Background Overlay → Color = `rgba(0,0,0,0.45)` → Opacity 1
- Inner container: Padding = 40px top/bottom, responsive reduce on mobile
- H1: white, bold, 56px desktop → 32px mobile
- Buttons: side-by-side on desktop, stacked Direction = Column on mobile viewport

---

## Tour Card (Grid Item)

### Structure
```
Flexbox Container (Direction = Column, Gap = 0)
  └── Hover state: box-shadow lifts, background shifts slightly
  ├── Image Widget (Object Fit = Cover, fixed height 220px)
  ├── Inner Container (padding 20px all sides)
  │   ├── Heading (H3) — tour name
  │   ├── Text Editor — 1 sentence description
  │   └── Flexbox Container (Direction = Row, Justify = Space Between, Align = Center)
  │       ├── Heading — price (e.g., "From $1,950")
  │       └── Button — "View Tour"
  └── Border Radius: 8px on all corners
```

### Hover Effect (No CSS)
Container → Style tab → Hover:
- Background Color: slightly lighter than default card color
- Box Shadow: `0 8px 24px rgba(0,0,0,0.12)`
- Transition Duration (Normal state): `0.25`

### Used In
- Homepage tour grid (3 columns)
- Tour category archive (Loop Builder)

---

## Tour Card Grid (3 Up)

### Structure
```
Grid Container (Columns = 3, Column Gap = 24px, Row Gap = 32px)
  └── [Repeat Tour Card × N]
```

### Responsive
- Tablet viewport: Columns = 2
- Mobile viewport: Columns = 1

---

## Inclusions / Exclusions Block (Two-Column)

### Structure
```
Flexbox Container (Direction = Row, Gap = 24px, Wrap = Wrap)
  ├── Flexbox Container (Direction = Column, Width = 50%)
  │   ├── Heading (H4) — "What's Included"
  │   └── Icon List Widget — green checkmark icons, one per inclusion
  └── Flexbox Container (Direction = Column, Width = 50%)
      ├── Heading (H4) — "Not Included"
      └── Icon List Widget — red X icons, one per exclusion
```

### Mobile
- On mobile viewport: each inner container → Width = 100% → stacks vertically

---

## Itinerary Day Block

### Structure
```
Flexbox Container (Direction = Row, Gap = 24px, Align Items = Flex Start)
  ├── Heading (H3, width = 80px) — "Day 1"
  └── Flexbox Container (Direction = Column, Gap = 8px)
      ├── Heading (H4) — Location / Theme
      ├── Text Editor — Morning activity
      ├── Text Editor — Afternoon activity
      └── Text Editor — Evening / Overnight
```

Use an Accordion widget to collapse/expand each day — reduces page length for long itineraries.

---

## WhatsApp + Call CTA Bar (Mobile Only)

### Structure
```
Flexbox Container (Direction = Row, Gap = 0, Position = Fixed, Bottom)
  ├── Button — "📞 Call Us" (width 50%, Dynamic Tags → Tel → +17727820494)
  └── Button — "💬 WhatsApp" (width 50%, Dynamic Tags → WhatsApp → +201201400578)
```

### Visibility
Advanced → Responsive → Hide on Device: check Desktop + Tablet (show Mobile only)

### Positioning
Advanced → Positioning → Position = Fixed, Vertical = Bottom, Horizontal = Left, Width = 100%
Advanced → Z-Index = 999 (above all other content)

---

## FAQ Block (Nested Accordion)

### Structure
```
Nested Accordion Widget
  ├── Item 1: "Is Egypt safe for Americans?"
  │   └── [Answer text]
  ├── Item 2: "What's the visa process?"
  └── Item 3: [etc.]
```

### Settings
- Default Active: First item open on load
- Style → Header → Background (closed): light sand color
- Style → Header → Background (open/active): brand primary color, white text
- Style → Content → Typography: Body font, 15px, 1.6 line height
- ARIA-compliant and keyboard-accessible out of the box

---

## Team Member Card

### Structure
```
Flexbox Container (Direction = Column, Align Items = Center)
  ├── Image Widget (Rounded, 120px × 120px, Object Fit = Cover)
  │   └── Border Radius = 50% (makes it circular)
  ├── Heading (H4) — Name
  ├── Text Editor — Role / Title
  └── Social Icons Widget — LinkedIn, Instagram, Email
```

### Hover Effect
Image widget → Style → Hover → CSS Filter → Brightness 110%
Container → Style → Hover → Box Shadow subtle lift

---

## Testimonial Section

### Structure
```
Flexbox Container (Direction = Column, Align Items = Center, Gap = 32px)
  ├── Heading (H2) — "What Our Travelers Say"
  └── Image Carousel Widget OR Flexbox Container (3-up Grid)
      └── [Each testimonial:]
          Flexbox Container (Direction = Column, Gap = 16px)
            ├── Text Editor — "Quote in quotation marks"
            ├── Star Rating Widget — e.g., 5.0
            └── Flexbox Container (Direction = Row, Align = Center, Gap = 12px)
                ├── Image Widget — traveler photo (circular, 48px)
                └── Flexbox Container (Direction = Column)
                    ├── Heading (H5) — Name
                    └── Text Editor — "Chicago, IL | Egypt Trip 2024"
```

---

## Pricing Block

### Structure
```
Flexbox Container (Direction = Row, Gap = 24px, Wrap = Wrap, Justify = Center)
  └── [For each pricing tier:]
      Flexbox Container (Direction = Column, Align = Center, Gap = 16px)
        ├── Heading (H4) — "Private Tour"
        ├── Heading (H2, accent color) — "$1,950 / person"
        ├── Text Editor — "Per person, double occupancy"
        ├── Icon List — what's included in this tier
        └── Button — "Request This Tour"
```

---

## Destination Map / Highlights Row

### Structure
```
Flexbox Container (Direction = Row, Gap = 32px, Justify = Center, Wrap = Wrap)
  └── [For each destination:]
      Flexbox Container (Direction = Column, Align = Center, Gap = 12px, Width = 20%)
        ├── Icon Widget — landmark icon (SVG) or Image
        ├── Heading (H5) — "Luxor"
        └── Text Editor — "2 nights"
```

Mobile: each item Width = 50% in mobile viewport (2 per row)

---

## Call-to-Action Section (Bottom of Tour Pages)

### Structure
```
Flexbox Container (Full Width, Background = brand color or dark image)
  └── Inner Container (Boxed, Direction = Column, Align = Center, Padding = 80px 20px)
      ├── Heading (H2) — "Ready to Experience Egypt?"
      ├── Text Editor — 1 sentence value proposition
      └── Flexbox Container (Direction = Row, Gap = 16px, Justify = Center)
          ├── Button — "Book This Tour" (Primary)
          └── Button — "Ask a Question" (Outlined, links to contact form anchor)
```

---

## Section Divider Between Content Areas

### Option 1: Shape Divider (No CSS)
Bottom section → Style → Shape Divider → Bottom → choose wave/curve → set color to match next section's background

### Option 2: Decorative Line
Divider widget: Style → Width = 80px, Color = accent, Weight = 2px, Gap = 40px

### Option 3: Spacing Only
Add padding-bottom to the upper section and padding-top to the lower section. Avoid using Spacer widgets inside Flex/Grid containers — use Container Gap instead.

---

## Image Background Section with Content Overlay

```
Flexbox Container (Full Width, Min Height = 500px)
  └── Style → Background → Image → Cover + Center
  └── Style → Background Overlay → Color = rgba(0,0,0,0.5), Opacity = 1
  └── Inner Container (Boxed, Direction = Column)
      ├── Heading — white text
      └── Text Editor — white text
```

**Always add a background overlay** — text on unoverlay'd photos is often illegible and fails contrast accessibility checks.

---

## Sticky "Book Now" Sidebar (Long Tour Pages)

```
Flexbox Container (Width = 320px, Position = Sticky, Top = 80px)
  ├── Heading — "Book This Tour"
  ├── Text — "From $1,950 per person"
  ├── Divider
  ├── Icon List — 3–4 key inclusions
  └── Button — "Request a Quote" (full width, links to form)
```

### Sticky Setup
Advanced → Motion Effects → Sticky → Top → Offset = 80 (clears sticky header)

Use inside a two-column Flexbox layout: left = itinerary content (wide), right = sticky booking card (narrow).

---

## Blog / Travel Tips Post Template (Theme Builder)

Built once, applies to all blog posts automatically.

```
Single Post Template:
  ├── Header (from Theme Builder Header)
  ├── Flexbox Container (Direction = Row, Gap = 40px)
  │   ├── Main Content (Width = 70%)
  │   │   ├── Image Widget → Dynamic Tag: Featured Image
  │   │   ├── Heading → Dynamic Tag: Post Title
  │   │   ├── Text Editor → Dynamic Tag: Post Content
  │   │   └── Author Box Widget → Dynamic: Author info
  │   └── Sidebar (Width = 30%)
  │       ├── "Book a Tour" CTA block (Global Widget)
  │       └── Recent Posts widget → "More Travel Tips"
  └── Footer (from Theme Builder Footer)
```
