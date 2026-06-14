# Elementor 3.21 — Editor Workflow Reference
### Navigation, shortcuts, copy/paste, templates, and the tools that save time

---

## Editor Layout

```
┌─────────────────────────────────────────────────────────┐
│  TOP BAR  [☰ Menu]  [Page Title]    [Responsive] [►]   │
├──────────────┬──────────────────────────────────────────┤
│              │                                          │
│  LEFT PANEL  │           CANVAS (live preview)          │
│              │                                          │
│  [Search]    │  ┌─────────────────────────────────┐    │
│  [Widgets]   │  │  Section / Container             │    │
│              │  │  ┌──────────┐  ┌──────────┐     │    │
│  When widget │  │  │ Widget   │  │ Widget   │     │    │
│  selected:   │  │  └──────────┘  └──────────┘     │    │
│  [Content]   │  └─────────────────────────────────┘    │
│  [Style]     │                                          │
│  [Advanced]  │                                          │
└──────────────┴──────────────────────────────────────────┘
```

---

## Navigator Panel

**Access:** Bottom toolbar → Navigator icon (list icon), or `Ctrl/Cmd + I`

Shows the full element tree of the page — every container, column, and widget in a collapsible tree. Indispensable for:
- Finding a widget buried inside nested containers
- Reordering elements by drag-and-drop in the tree (easier than dragging on the canvas)
- Clicking to select elements that are hard to click on the canvas (overlapping, transparent, etc.)
- Renaming elements: double-click the element name in Navigator to give it a human-readable label (e.g., "Hero Section", "Tour Card Grid")

**Tip:** Name your containers in Navigator as you build. When you come back to edit a page with 50 elements, named containers save enormous time.

---

## Keyboard Shortcuts (Elementor 3.21)

### Selection and Navigation
| Shortcut | Action |
|---|---|
| `Esc` | Deselect / move selection up to parent |
| `Ctrl/Cmd + I` | Open/close Navigator |
| `Ctrl/Cmd + F` | Find (search for text content or widget type on the page) |

### Editing
| Shortcut | Action |
|---|---|
| `Ctrl/Cmd + Z` | Undo |
| `Ctrl/Cmd + Shift + Z` | Redo |
| `Ctrl/Cmd + C` | Copy selected element (with all settings) |
| `Ctrl/Cmd + V` | Paste element |
| `Ctrl/Cmd + D` | Duplicate selected element |
| `Del` or `Backspace` | Delete selected element (with confirmation) |

### Saving and Publishing
| Shortcut | Action |
|---|---|
| `Ctrl/Cmd + S` | Save (draft — does not publish) |
| `Ctrl/Cmd + Shift + S` | Save as Template |
| `Ctrl/Cmd + P` | Preview in new tab |

### View Controls
| Shortcut | Action |
|---|---|
| `Ctrl/Cmd + Shift + H` | Toggle editor/page-only view (hide left panel) |
| `Ctrl/Cmd + Shift + M` | Toggle responsive mode |

---

## Right-Click Context Menu

Right-click any element on the canvas to access:

| Option | What it does |
|---|---|
| **Edit [Widget Name]** | Opens its settings panel |
| **Duplicate** | Creates a copy immediately below |
| **Copy** | Copies the element and all its settings |
| **Paste** | Pastes the copied element |
| **Paste Style** | Applies ONLY the style settings from the copied element to the selected element — keeps the content, changes the look |
| **Reset Style** | Reverts all style settings to defaults |
| **Copy & Paste Cross-Site** | Copies JSON to clipboard — paste into another WordPress site running Elementor |
| **Save as Template** | Saves to your Template Library for reuse |
| **Delete** | Removes the element |

**"Paste Style" is extremely useful** — design one card, then paste its style onto other cards without re-entering content. Huge time saver.

---

## Copy/Paste Across Pages and Sites

### Same Site (Different Pages)
1. Right-click element → Copy
2. Open the other page in Elementor
3. Right-click → Paste (or `Ctrl/Cmd + V`)

Settings, styles, and content all transfer.

### Cross-Site (Different WordPress Installations)
1. Right-click → **Copy & Paste Cross-Site** → Copy Element
2. On the target site, open any page in Elementor
3. Right-click → **Copy & Paste Cross-Site** → Paste

Useful when building a new tour page on staging and then transferring it to production.

---

## Template Library

### Saving a Template
- Right-click any element (widget, container, section) → **Save as Template**
- Give it a clear name: "Tour Card — Cairo", "Hero — Nile Cruise Page", "FAQ Block"
- Saved templates appear in `Templates → Saved Templates`

### Using a Template
- Click the **folder icon** in any empty section to browse templates
- Or: drag any widget/container, then replace it with a template via the folder icon in the empty state

### Syncing Templates Across Sites
`Site Settings → Import / Export Kit`
- Export selected templates, global colors, global fonts, theme style as a `.zip`
- Import into another site — design system travels with it

---

## Revision History

**Access:** Bottom toolbar → History icon (clock icon), or `Ctrl/Cmd + Shift + H` after navigating.

Elementor auto-saves a revision every time you manually save. The panel shows:
- Timestamp of each revision
- Who made it (if multiple editors)
- Click any revision to preview it
- Click **Apply** to restore to that version

**Recommendation:** Before a major redesign of a page, save first — creates a clean restore point.

---

## Global Widgets

**Creating:** Right-click any widget → Save as Global

**Editing:** Click the widget → the panel shows "Edit Global" banner → click it → changes propagate to all instances across the site

**Converting back:** Right-click a global widget → Unlink from Global — creates a local copy without removing the global version

---

## Notes Feature (New in 3.21)

**Access:** Bottom toolbar → Notes icon (speech bubble)

Allows you to leave sticky notes on specific elements for other team members or for yourself. Notes are visible in the editor but don't appear on the frontend.

Use for:
- "TODO: replace placeholder image with real photo from Shereef"
- "Client asked to change this heading — waiting for approval"
- Flagging elements that need content updates before publishing

Notes are visible to anyone who opens the page in Elementor.

---

## Find & Replace

**Access:** `Ctrl/Cmd + F` in the editor

Finds text content across all widgets on the current page. Useful for:
- Finding all instances of an old phone number before updating
- Locating which widget contains specific text when the page has 30+ widgets
- Searching by widget type

**Note:** Find works within the current page only — not across the entire site.

---

## Editor Top Bar (Beta in 3.21)

An experimental redesigned top navigation bar. Enable via:
`WP Admin → Elementor → Settings → Experiments → Editor Top Bar → Active`

Moves some panel controls to a cleaner top bar. If it causes issues with any Pro features, deactivate and revert to the standard toolbar.

---

## Page Settings

**Access:** Bottom toolbar → Settings icon (gear icon) → Page Settings

| Setting | Purpose |
|---|---|
| **Page Layout** | Elementor Canvas (blank page), Elementor Full Width (no sidebar), Default (theme layout) |
| **Hide Title** | Hides the default WordPress page title — always turn ON for pages built fully in Elementor |
| **Status** | Draft / Published / Private |
| **Featured Image** | Page thumbnail (used for social sharing preview) |
| **Body Background** | Override the theme's body background for this page only |

**Always set Page Layout to "Elementor Canvas" or "Elementor Full Width" for new tour pages** — otherwise the theme's sidebar, header, or footer may appear outside of your Elementor-designed header/footer.

---

## Container Width Settings

### Content Width (Global)
`Site Settings → Layout → Content Width`
Sets the maximum width for page content across the site (e.g., `1200px`). This is the baseline all pages inherit.

### Per-Container Width
Each container has its own width setting:
- **Boxed:** respects the global content width
- **Full Width:** stretches to 100% of the browser window
- **Custom:** set a specific pixel or percentage width

Hero sections and background image sections should be **Full Width**.
Content columns inside them should be **Boxed** or a specific max-width.

---

## Breakpoints (Responsive Editing)

**Access:** `Site Settings → Layout → Breakpoints`

Default breakpoints in Elementor 3.21:
| Device | Default breakpoint |
|---|---|
| Desktop | Above 1024px |
| Tablet | 768px – 1024px |
| Mobile | Below 768px |

### Custom Breakpoints (Pro)
Add up to 6 custom breakpoints (e.g., `1440px` for large monitors, `480px` for small phones).
Each custom breakpoint gets its own viewport tab in responsive editing mode.

**When to add a breakpoint:**
- Design breaks significantly at a size not covered by the default three
- Client has analytics showing heavy traffic from a specific screen size (e.g., iPads in landscape)

---

## Saving Workflow (Recommended)

1. **While building:** `Ctrl/Cmd + S` frequently — saves as draft
2. **Before major change:** Save → check Revision History timestamp
3. **Before publishing:** Preview in new tab → test on mobile viewport → check all links
4. **Publish:** Update button (top of left panel) or via WordPress MCP
5. **After publishing:** Check the live URL on a real device — editor preview is not 100% accurate for every font load and animation

---

## Common Editor Mistakes to Avoid

- **Closing the editor without saving** — Elementor does NOT auto-save every action, only on manual save. `Ctrl/Cmd + S` often.
- **Editing on the live page without staging** — Major structural changes should be tested on a staging copy first.
- **Forgetting to check Mobile viewport** — The canvas defaults to Desktop. Always click the Mobile icon before marking a page done.
- **Publishing without checking the page title visibility** — Many pages accidentally show the default WordPress title above the Elementor design. Set `Page Settings → Hide Title → Yes`.
- **Adding custom CSS in the wrong place** — Global CSS goes in `Site Settings → Custom CSS`. Element-specific CSS goes in that element's `Advanced → Custom CSS`. Mixing these causes specificity conflicts.
