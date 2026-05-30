# VOID UI — Open Design Documentation

**A minimalist icon pack designed in the open. Pure aesthetics. Zero compromise.**

---

## What is VOID UI?

VOID UI is a **minimalist monoline icon pack** optimized for AMOLED displays. Every icon is crafted on a pure black background (#000000) with crisp white strokes (#FFFFFF), creating a premium, editorial aesthetic that's both functional and beautiful.

**Core values:**
- 🖤 **Pure black AMOLED efficiency** — battery-friendly, high contrast
- ✨ **Consistent monoline design** — 3-4px strokes, pixel-perfect grid alignment
- 🎯 **Semantic icon matching** — form follows function, never decoration for decoration's sake
- 🔧 **Open design process** — documented, iterative, community-informed

---

## By the Numbers

| Metric | Count |
|--------|-------|
| **Free Tier Icons** | 288 (VOID UI core) |
| **Premium Packs** | 5 themed packs (568 icons) |
| **Total Coverage** | 856+ icons across all tiers |
| **Design Tools** | Figma (design) + SVG (master) + XML (Android) |
| **Supported Platforms** | Android 8.0+ (26+) |
| **Supported Launchers** | 7 major launchers (Nova, Niagara, Apex, etc.) |

---

## Design Philosophy

### 1. Pure Black Backgrounds

Every icon sits on `#000000` (pure black). This isn't a stylistic choice—it's functional:
- **AMOLED efficiency:** Pure black pixels consume minimal power on organic LED screens
- **High contrast:** White strokes on black deliver maximum readability
- **Premium perception:** Minimalist black = editorial, luxury, intentional design

### 2. Monoline Aesthetics

All icons use a single stroke weight (3-4px), applied consistently:
- **No filled shapes** — strokes only, creating negative space
- **Rounded linecaps & joins** — soft, friendly feel without hard corners
- **Grid alignment** — every stroke sits on pixel boundaries (no 0.5px antialiasing artifacts)

### 3. Semantic Coverage

Icons are organized by semantic meaning, not alphabetically or by source:
- **AI & Models** (Claude, ChatGPT, Gemini, etc.)
- **Social & Messaging** (Instagram, Twitter, Discord, etc.)
- **Productivity & Work** (Google Workspace, Notion, Asana, etc.)
- **Media & Entertainment** (Spotify, Netflix, YouTube, etc.)
- **Finance & Commerce** (PayPal, Stripe, Crypto, etc.)
- **And 8 more categories** (see full breakdown in ICON_INVENTORY.md)

Each category groups related apps so users can quickly find thematically similar icons.

### 4. Premium Packs as Aesthetic Themes

Rather than a single "dark mode" or "colorful mode," VOID UI launches **5 premium packs** with distinct visual languages:

| Pack | Aesthetic | Use Case |
|------|-----------|----------|
| **CIRCUITRY** | Neon circuit board | Tech enthusiasts, developers |
| **TERMINAL** | Retro amber CRT | Hacker aesthetic, retro fans |
| **XENOCOMM** | Alien bioluminescent | Sci-fi fans, futurists |
| **CRICKET NATIONS** | Geometric abstraction | Sports fans, regional pride |
| **SPORTS ZONES** | Runtime colour-adaptive | Fantasy league, team apps |

Each pack is **a complete design system**, not just a recolor. They demonstrate different ways to extend the VOID UI philosophy.

---

## Icon Categories (288 Core Icons)

### 🟣 AI & Models (45 icons)
Claude, ChatGPT, Gemini, Grok, Copilot, Perplexity, Mistral, DeepSeek, Midjourney, Runway, Descript, Hugging Face, and more. Covers major LLMs, generative AI, and ML platforms.

### 🩵 Social & Messaging (25 icons)
Instagram, TikTok, Twitter/X, Reddit, Bluesky, Threads, Mastodon, WhatsApp, Telegram, Signal, Discord, Slack, and more. Full coverage of modern social networks and messaging platforms.

### 📧 Email & Inbox (18 icons)
Gmail, Outlook, Mail, inbox management utilities. Includes compose, send, archive, spam, and folder icons.

### 🟢 Productivity & Work (35 icons)
Google Workspace, Microsoft 365, Notion, Asana, Trello, Monday, Jira, Figma, Framer, Webflow, Baserow, Airtable, Coda, and more. Full office suite coverage.

### 🩷 Media & Entertainment (22 icons)
Netflix, Prime Video, Disney+, Spotify, Apple Music, YouTube, Tidal, Pandora, and streaming services. Plus video editing and podcast apps.

### 🟡 Finance & Commerce (19+ icons)
Stripe, PayPal, Wise, Revolut, Crypto exchanges, banking apps, e-commerce platforms. Covers payments, investments, and shopping.

### 🔵 Tech & Connectivity (20 icons)
AWS, Azure, GCP, GitHub, GitLab, Docker, Kubernetes, CI/CD platforms, npm, and developer tools.

### ⚪ Navigation & UI (45 icons)
System controls, gestures, page transitions, UI elements. Includes home, back, menu, settings, search, toggle, expand/collapse, and more.

### 🟤 Files & Storage (8 icons)
Google Drive, Dropbox, OneDrive, iCloud, Nextcloud, and file management utilities.

### 🟢 Maps & Travel (10 icons)
Google Maps, Apple Maps, Waze, Uber, Lyft, Airbnb, Booking, Expedia, and travel platforms.

### 🔴 Health & Lifestyle (12 icons)
Fitness trackers, meditation apps, health monitoring, wellness platforms.

### 🟣 People & Security (16 icons)
Contacts, authentication, VPN, privacy, biometric, password management.

### ⚫ Uncategorised (12 icons)
Generic utilities, widgets, and miscellaneous system icons.

---

## Design Files & Resources

### Primary Design Files

| Resource | Location | Purpose |
|----------|----------|---------|
| **Figma** | [VOID UI Icon Pack](https://www.figma.com/design/4kszGYksUUIETAxL7mcXvM) | Live design, 291 core icons organized by category |
| **ICON MASTER** | `C:\Users\User\CLAUDE\ICON MASTER\` | 1,394 master SVGs across 9 series |
| **GitHub** | [angusm99/VOID_UI_Android](https://github.com/angusm99/VOID_UI_Android) | Android implementation, 856 VectorDrawable XMLs |

### Documentation

| Doc | Audience | Purpose |
|-----|----------|---------|
| **ICON_INVENTORY.md** | Designers, developers | Complete 856-icon reference with categories |
| **OPEN_DESIGN.md** | Design community | This document — open design philosophy |
| **Design Rules** | Designers | Stripe widths, grid, accent colours per pack |
| **Premium Pack Specs** | Pack implementers | CIRCUITRY neon, TERMINAL amber, XENOCOMM cyan |

---

## How to Use VOID UI

### For Android Users (Players)

1. Install VOID UI from Google Play Store (free tier, 288 icons)
2. Open your launcher (Nova, Niagara, Apex, etc.)
3. Go to **Settings → Themes/Icon Packs**
4. Select **VOID UI**
5. Optionally unlock premium packs (Circuitry, Terminal, Xenocomm, etc.) via IAP

### For Designers (Community)

**Option A: Draw on top of Figma**
1. Duplicate VOID UI Figma file (request access at GitHub)
2. Use as a design system foundation
3. Create your own branded variant

**Option B: Adapt ICON MASTER SVGs**
1. Clone the [GitHub repo](https://github.com/angusm99/VOID_UI_Android)
2. Download individual SVGs from `ICON MASTER/` folders
3. Modify in Illustrator, Affinity, or Inkscape
4. Submit PR to contribute back

**Option C: Study the Design System**
1. Download full ICON MASTER library
2. Analyze stroke weights, grid alignment, accent colours
3. Create your own icon pack inspired by (but not copying) VOID UI
4. Reference VOID UI in your design docs

### For Developers (Pack Builders)

1. Fork [GitHub repo](https://github.com/angusm99/VOID_UI_Android)
2. Reference `docs/Design Rules` for each pack's specifications
3. Follow SVG → VectorDrawable XML conversion process (documented in repo)
4. Implement as Android drawable resources
5. Submit PR with new pack

---

## Premium Packs Specifications

### CIRCUITRY (94 icons)

**Visual Identity:**
- Stroke width: 14px
- Stroke linecap: round
- Terminal dots at endpoints: filled circles, r="9"
- Default accent: `#00FF41` (matrix green)
- Theme: Neon circuit board, tech aesthetic

**Design Process:**
1. Start with VOID UI core skeleton
2. Thicken strokes to 14px
3. Add filled circles at line endpoints
4. Apply neon green to key elements
5. Test on AMOLED black background

### TERMINAL (108 icons)

**Visual Identity:**
- Stroke width: 3-4px (same as core)
- Stroke linecap: 90° (no rounding)
- Double-line CRT effect: two parallel strokes, second at 40% opacity
- Default accent: `#FFB000` (amber)
- Phosphor glow: SVG filter with feGaussianBlur stdDeviation="3"
- Theme: Retro amber CRT, hacker aesthetic

**Design Process:**
1. Start with VOID UI skeleton
2. Change stroke ends to 90° corners
3. Duplicate strokes (one at 40% opacity for glow)
4. Apply amber colour
5. Add Gaussian blur filter element

### XENOCOMM (123 icons)

**Visual Identity:**
- Primary: Cyan `#00FFE5`
- Secondary: Violet `#9D4EDD`
- Geometry: Mix of organic curves + crystalline shapes
- Theme: Alien bioluminescent, sci-fi futurism

**Design Elements:**
- Tentacle variants (curved, twisted, branching, segmented)
- Eye variants (10+ unique alien eye designs)
- Portal/gateway shapes
- Organism parts (spine, exoskeleton, carapace)
- Energy states (condensing, dispersing, phasing)

### CRICKET NATIONS (16 icons)

**Visual Identity:**
- Geometric abstraction of cricket nations
- Team-specific colour variants applied at runtime
- Icons for: India, Australia, Pakistan, England, South Africa, West Indies, Sri Lanka, New Zealand, Bangladesh, Afghanistan, Netherlands, Ireland, Zimbabwe, Namibia

### SPORTS ZONES (30 icons)

**Visual Identity:**
- Runtime colour substitution system
- Three placeholder values in SVG:
  - `ZONE_PRIMARY` → team primary colour
  - `ZONE_SECONDARY` → team secondary colour
  - `ZONE_ACCENT` → highlight/trim colour
- Enables unlimited team customization at runtime

**Icon Types:**
- Ball sports (cricket, football, basketball, soccer, etc.)
- Player positions (batter, bowler, keeper, fielder, etc.)
- Team elements (jersey, captain armband, trophy, scoreboard)
- Referee & officials (whistle, flag, penalty card)
- Equipment (bat, glove)

---

## Contributing to VOID UI

### Suggest an Icon

1. Open [GitHub Issues](https://github.com/angusm99/VOID_UI_Android/issues)
2. Title: `[Icon Request] App Name`
3. Include:
   - App name & icon (screenshot or link)
   - Why it should be included (popular, emerging, underrepresented category)
   - Suggested category (e.g., "AI & Models" or "Social & Messaging")

### Contribute Icons

1. Fork the repository
2. Add SVG to appropriate `ICON MASTER/XX_SERIES/` folder
3. Follow design specs (stroke width, grid alignment, accent colours)
4. Test rendering on black background
5. Submit PR with:
   - Icon previews
   - Category classification
   - Rationale for inclusion

### Suggest a Pack Theme

1. Open [GitHub Issues](https://github.com/angusm99/VOID_UI_Android/issues)
2. Title: `[Pack Idea] Theme Name`
3. Include:
   - Visual concept (what aesthetic, what colour scheme)
   - Use cases (who would want this pack?)
   - 3-5 example icons in the proposed style

---

## Figma Access & Community

**Figma File:** [VOID UI — Icon Pack](https://www.figma.com/design/4kszGYksUUIETAxL7mcXvM)

**Sharing:**
- Design foundations are **open for reference and study**
- Duplication requires contributor approval (to maintain design coherence)
- Community members can propose variants for inclusion

**Feedback:**
- File comments enabled (Figma)
- GitHub Issues for feature requests
- Pull Requests for contributions

---

## Design Principles (TL;DR)

1. **Form Follows Function** — Icons communicate, don't decorate
2. **Consistency Over Novelty** — Unified stroke weight, grid, proportions
3. **Efficiency Through Minimalism** — Black pixels save power on AMOLED
4. **Community-Informed** — Designed with and for designers, developers, users
5. **Open & Evolving** — Master library grows with community contributions
6. **Semantic Organization** — Icons grouped by meaning, not alphabetically
7. **Premium Packs as Themes** — Each pack is a complete design system, not a recolor

---

## Files & Structure

```
VOID UI (GitHub)
├── app/src/main/res/
│   ├── drawable/                  (856 VectorDrawable XMLs — framed)
│   ├── drawable-nodpi/            (733 bare icons)
│   ├── mipmap-*/                  (launcher icons for all densities)
│   └── xml/appfilter.xml          (launcher mappings)
├── docs/
│   ├── ICON_INVENTORY.md          (complete icon reference)
│   ├── OPEN_DESIGN.md             (this file)
│   ├── Design Rules               (pack specifications)
│   ├── PLAY_STORE_LISTING.md
│   ├── privacy-policy.md
│   └── ...more docs
└── ICON MASTER (sister folder)
    ├── 01_APP_ICONS/              (188 SVGs)
    ├── 02_VOID_UI/                (195 SVGs)
    ├── 03_MANUS_CIRCUIT/          (210 SVGs)
    ├── 04_SYSTEM_UICONS/          (430 SVGs)
    ├── 05_CIRCUITRY/              (94 SVGs)
    ├── 06_TERMINAL/               (108 SVGs)
    ├── 07_CRICKET_NATIONS/        (16 SVGs)
    ├── 08_SPORTS_ZONES/           (30 SVGs)
    └── 09_XENOCOMM/               (123 SVGs)
```

---

## License & Attribution

**VOID UI is open source.**

- **Code:** [MIT License](https://github.com/angusm99/VOID_UI_Android/blob/master/LICENSE)
- **Icons:** Creative Commons (attribution required for derivatives)
- **Free Tier:** Use freely on Android devices via the app
- **Premium Packs:** In-app purchase on Google Play
- **Master Library:** Available for study, customization, community contribution

**Attribution:**
If you create a derivative pack or reference VOID UI in your design system, please credit:
```
Design inspired by VOID UI (github.com/angusm99/VOID_UI_Android)
```

---

## Links & Resources

| Resource | URL |
|----------|-----|
| **GitHub** | https://github.com/angusm99/VOID_UI_Android |
| **Figma Design** | https://www.figma.com/design/4kszGYksUUIETAxL7mcXvM |
| **Google Play Store** | Coming soon (2026-05) |
| **Issues & Requests** | https://github.com/angusm99/VOID_UI_Android/issues |
| **Contact** | angusm99@gmail.com |

---

## FAQ

**Q: Can I use VOID UI icons in my own app?**  
A: Yes! VOID UI is designed to be freely used and extended. Download SVGs, adapt them, credit VOID UI in your app description.

**Q: Can I contribute my own icons?**  
A: Absolutely. Open a PR on GitHub with your SVG designs. Follow design specs (stroke width, grid alignment, black background) for consistency.

**Q: How do I convert SVGs to Android VectorDrawables?**  
A: The repo includes conversion scripts and documentation. See ICON MASTER → `generate_all.py` and the Android project build process.

**Q: Will there be more premium packs?**  
A: Yes! Community contributions are welcome. Propose your pack idea as a GitHub issue.

**Q: What about iOS/macOS/Windows icons?**  
A: Currently Android-focused. If you want to port VOID UI to other platforms, open an issue—contributions welcome.

**Q: How often are new icons added?**  
A: Monthly updates (bi-weekly for urgent requests). Keep an eye on GitHub releases.

---

## Credits

- **Design & Development:** [Angus Miller](https://github.com/angusm99)
- **Community Contributors:** [See GitHub](https://github.com/angusm99/VOID_UI_Android/graphs/contributors)
- **Special Thanks:** Claude AI (design assistant), Figma team, Android community

---

**Made with precision and care for minimalist design.**  
Pure black. Pure white. Pure intent.

🖤

---

**Last Updated:** 2026-05-29  
**Status:** Open for contributions  
**Version:** 1.8
