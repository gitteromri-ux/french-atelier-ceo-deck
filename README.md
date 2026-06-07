# French Atelier · CEO Marketing Review Deck

Premium minimal CEO presentation deck for French Atelier, built as a static horizontal-scroll gallery experience.

---

## Design System

| Token | Value | Role |
|---|---|---|
| `--color-cream` | `#F5EFE6` | Default slide background |
| `--color-navy` | `#0A1128` | Cover, section dividers, closing |
| `--color-gold` | `#C9A961` | Accent — rules, dots, eyebrow labels |
| `--color-ink` | `#0C0D10` | Primary text |
| `--color-muted` | `#5B6474` | Secondary text |
| `--color-border` | `#E5DFD3` | Dividers, card borders |

**Fonts** — Cormorant Garamond (display/headlines) + Inter (body/UI), loaded from Google Fonts.

---

## File Structure

```
web/
├── index.html          Main entry point
├── css/
│   └── deck.css        Full design system + slide layout
├── js/
│   └── deck.js         Navigation, counters, fullscreen, touch
└── README.md           This file
```

---

## Navigation

| Action | Result |
|---|---|
| `→` / `↓` / `Page Down` | Next slide |
| `←` / `↑` / `Page Up` | Previous slide |
| `Home` | First slide |
| `End` | Last slide |
| `F` key | Toggle fullscreen |
| Click dot | Jump to slide |
| Swipe left/right | Navigate (touch) |
| Scroll horizontally | Navigate (mouse/trackpad) |

---

## Slide Variants

- `.slide--cream` — Warm cream `#F5EFE6` (default content slides)
- `.slide--dark` — Deep navy `#0A1128` (cover, section dividers, closing)
- `.slide--white` — Light paper `#FDFAF6` (alternate content slides)

---

## Adding Slides

Add a `<section class="slide slide--cream" data-slide="N" id="slide-N">` block inside `<main class="deck">`. The dot navigation and counter update automatically via JS — no manual changes required.

---

## PDF Download

Place the exported PDF at the web root as `French_Atelier_CEO_Deck.pdf`. The PDF button in the header links to `/French_Atelier_CEO_Deck.pdf`.

---

## Local Preview

```bash
# Using Node `serve` (recommended)
npx serve . -l 3000

# Or Python
python3 -m http.server 3000
```

Then open `http://localhost:3000`.

---

*Confidential · French Atelier · June 2026*
