# Frequently Asked Questions (FAQ)

For VOID UI users and curious folks. Updated as new questions come in.

---

## Installation & Setup

### How do I install VOID UI?

1. Search "VOID UI" on Google Play Store
2. Tap **Install**
3. Wait for download (~6 MB)
4. Open the app to verify

### How do I apply VOID UI to my launcher?

Different launchers have different methods:

**Nova Launcher:**
- Open Nova Launcher → Settings (3 dots)
- Look & feel → Icon style → Icon theme
- Select **VOID UI**

**Niagara Launcher:**
- Open Niagara Launcher → Settings
- Look → Icon Theme → Select **VOID UI**

**Apex Launcher:**
- Open Apex → Settings → Theme settings → Icon theme
- Select **VOID UI**

**Samsung One UI (Galaxy):**
- Long-press home screen → Themes
- Tap **Icons** tab → Find VOID UI → **Apply**

**Other launchers:** Usually under Settings → Themes or Icon Pack

### My launcher doesn't show VOID UI in the icon theme list

This usually means:
- The launcher doesn't support icon packs (rare)
- VOID UI installation didn't complete
- Try restarting the launcher app

**Solution:**
1. Force close your launcher
2. Reopen it
3. Check icon themes again

### Will VOID UI work on my phone?

VOID UI requires:
- Android 8.0 (Oreo) or higher
- ~10 MB free storage
- Compatible launcher (most are supported)

If you have Android 8.0+, it should work. Tested on:
- Samsung Galaxy S20-S24
- Pixel 3-9
- OnePlus 9-12
- Other major brands

---

## Icons & Apps

### How many icons does VOID UI include?

- **Free tier:** 288 branded icons + system icons
- **Premium packs:** 568 additional icons (5 packs)
- **Total available:** 856 icons across all tiers

### Does VOID UI have an icon for [specific app]?

VOID UI includes icons for popular apps in these categories:
- AI/ML (Claude, ChatGPT, Gemini, Grok, Copilot)
- Social media (Instagram, Twitter, TikTok, Reddit)
- Productivity (Notion, Slack, Office, Drive)
- Media (Spotify, YouTube, Netflix)
- Finance, gaming, navigation, fitness

For specific apps not listed, please:
1. Check Settings → Variants for v1, v2, v3 alternatives
2. Submit a request on [GitHub Issues](https://github.com/angusm99/VOID_UI_Android/issues/new?template=missing_icon.md)

We add 10-20 new icons in each update based on user requests.

### Why is some app's default icon showing instead of the VOID UI version?

This is normal! It happens when:
1. **App not in appfilter.xml** — we haven't mapped it yet
2. **App has a custom system icon** — some apps don't use icon packs
3. **Launcher cache** — restart your launcher

**Solution:** Open launcher settings → Icon themes → Re-apply VOID UI

### Can I request a specific icon style for an app?

Yes! When submitting an [icon request](https://github.com/angusm99/VOID_UI_Android/issues/new?template=missing_icon.md), include:
- App name and package name
- Brief description of desired style
- Reference images if available
- Multiple variant requests welcome

---

## Premium Packs

### What are the premium packs?

5 themed icon packs available as In-App Purchase:

**CIRCUITRY** — Neon circuit board aesthetic with glowing matrix green endpoints  
**TERMINAL** — Retro amber CRT phosphor glow on black, 90° geometry  
**XENOCOMM** — Alien bioluminescent cyan and violet, sci-fi futurism  
**CRICKET NATIONS** — Geometric nation symbols for cricket fans  
**SPORTS ZONES** — Runtime colour-adaptive team icons  

### Are premium packs expensive?

**Individual packs:** $0.99 - $2.99 USD  
**All-In-One Bundle:** $5.99 USD (saves 30%)

Pricing varies by region (Play Store auto-converts).

### Can I use premium packs without purchase?

No, premium packs are locked until purchased. The free tier (288 icons) is generous and covers most popular apps.

### Will premium packs ever go on sale?

We may run occasional sales (holidays, app birthday). Follow us on Twitter/X (@VOID_UI) for announcements.

### Can I get a refund?

Yes! Google Play allows refunds within 48 hours of purchase. Just go to:
1. Play Store → My orders → Find your VOID UI purchase
2. Tap **Refund**
3. Reason: Whatever applies

### Do premium packs work on multiple devices?

Yes! Premium packs are tied to your Google Play account, not a specific device. Sign in with the same Google account on any device.

To restore on a new device:
1. Install VOID UI from Play Store
2. Open Settings → **Restore Purchases**
3. Premium packs unlock

---

## Privacy & Security

### Does VOID UI collect any data?

**No.** Zero data collection.

VOID UI does not:
- Collect personal information
- Track usage or analytics
- Show ads
- Use third-party SDKs
- Require an account
- Connect to the internet

Pure design asset with zero data handling.

### Does VOID UI require permissions?

**No permissions required.** VOID UI is configured entirely in AndroidManifest.xml with launcher intent-filters.

Apps that need permissions (camera, contacts, etc.) request them at install. VOID UI requests zero.

### Is VOID UI safe to install?

Yes. It's open-source and reviewed:
- [GitHub source code](https://github.com/angusm99/VOID_UI_Android)
- No analytics or tracking code
- No suspicious permissions
- Reviewed by Google Play before publication
- MIT licensed

### What happens if I uninstall VOID UI?

- All icon themes return to launcher defaults
- No data is lost (we don't store data)
- All purchased premium packs remain in your account
- Can reinstall later and continue

---

## Technical Questions

### What's a VectorDrawable?

VectorDrawable is Android's standard format for scalable graphics. They're resolution-independent and look crisp on any screen size.

VOID UI uses 856 VectorDrawable XML files (converted from original SVG designs).

### Why are some icons different sizes?

All icons are 108×108dp (standard Android adaptive icon size). They scale automatically based on your device's DPI.

If icons look small/large compared to other apps:
- Your launcher may have icon size settings
- Try adjusting in launcher → settings → icon size

### Can I customize the icon colors?

Currently, no — colors are set per pack:
- Free tier: white strokes on black
- Premium packs: each has its own accent color

In v1.4+ we plan to add user-customizable accent colors.

### What launchers are supported?

VOID UI works with 9 launcher types:

1. Nova Launcher
2. Niagara Launcher
3. Apex Launcher
4. Action Launcher
5. ADW Launcher
6. Lawnchair
7. Atom Launcher
8. Tesla Launcher
9. Samsung One UI

Most other launchers should also detect VOID UI automatically.

---

## Updates & Support

### How often does VOID UI update?

We release updates every 4-6 weeks with:
- New icons (10-20 per update)
- Bug fixes
- Performance improvements
- New premium packs (when available)

### How do I update VOID UI?

If you have auto-update enabled:
- VOID UI updates automatically through Play Store

To manually update:
1. Open Play Store
2. Search "VOID UI"
3. Tap **Update** if available

### Will my custom icon assignments be preserved during updates?

Custom assignments are stored in your launcher, not in VOID UI. Updates won't affect them.

If you assigned a specific icon to an app manually, that mapping remains.

### How do I contact support?

**Best ways to reach us:**

1. **GitHub Issues** (for bugs, feature requests):
   https://github.com/angusm99/VOID_UI_Android/issues/new

2. **Email** (for questions or feedback):
   angusm99@gmail.com

3. **Play Store Reviews** (for general comments):
   Reply to your review and we'll respond

### Why isn't my issue/request being addressed?

We aim to respond within 48 hours:
- Bug reports: Investigate and fix in next update
- Icon requests: Add if popular and feasible
- Feature requests: Considered for future roadmap

If urgent, mark issue with "urgent" label or email directly.

---

## Comparison With Other Icon Packs

### How is VOID UI different from [other icon pack]?

VOID UI's strengths:
- **AMOLED-optimized** — pure black saves battery
- **Zero data collection** — no analytics, no ads, no tracking
- **Premium pack variety** — 5 distinct aesthetic themes
- **Samsung One UI compatibility** — many icon packs miss this
- **Open source** — code is public on GitHub
- **Solo developer** — direct, honest communication

VOID UI's limitations:
- **Currently smaller library** than some commercial packs (856 vs. 10,000+)
- **No live wallpaper** (yet)
- **No custom icon editor** (yet)
- **Only Android** (no iOS version yet)

### Should I use VOID UI or [other icon pack]?

Choose VOID UI if you:
- Value privacy and zero data collection
- Want clean, minimalist aesthetic
- Use AMOLED devices and want battery savings
- Like the option of premium themed packs (Circuitry, Terminal, etc.)
- Want active development with regular updates

Choose other packs if you:
- Need 10,000+ icon library immediately
- Want extensive customization (color, size, etc.) per-icon
- Prefer flat or rounded icon style over monoline

---

## Get Involved

### Can I contribute to VOID UI?

Yes! We welcome contributions:

**Code contributions:** 
- Fork the [GitHub repo](https://github.com/angusm99/VOID_UI_Android)
- Make improvements
- Submit a pull request

**Icon design contributions:**
- Email design suggestions
- Submit via GitHub issue
- (Possible future: revenue share for accepted designs)

**Bug reports & feature requests:**
- Open issues on GitHub
- Help us improve VOID UI for everyone

### How do I support VOID UI?

If you find VOID UI useful, please:

1. **Leave a Play Store review** (5★ helps a lot!)
2. **Share with friends** (word of mouth = our best marketing)
3. **Star on GitHub** (helps with discoverability)
4. **Buy premium packs** (funds future development)
5. **Submit icon requests** (helps us prioritize)

---

## Privacy Policy & Legal

### Where can I read your privacy policy?

[Read full privacy policy](https://angusm99.github.io/VOID_UI_Android/privacy-policy.md)

Short version: We don't collect data. Pure design asset.

### Is VOID UI GDPR compliant?

Yes! VOID UI is fully GDPR/CCPA/COPPA compliant because we don't process any personal data.

### What's your data retention policy?

We don't have one — we don't collect data, so there's nothing to retain.

### Who's behind VOID UI?

Hi, I'm Angus! I'm a solo developer/designer based in Cape Town, South Africa. VOID UI started as a personal project to learn Android development and design.

If you have questions, suggestions, or just want to chat about Android themes:
- Email: angusm99@gmail.com
- GitHub: [@angusm99](https://github.com/angusm99)

---

## Future Updates

### What's coming in v1.3?

- **Premium pack IAP** (purchase packs for $0.99-$2.99)
- **15-20 new icons** based on user requests
- **Settings activity** (in-app pack selection)
- **Restore purchases** button

Target: 4-6 weeks after launch

### What about v1.4 and beyond?

See our [roadmap](https://github.com/angusm99/VOID_UI_Android/blob/master/docs/V1_3_ROADMAP.md) for the full plan.

---

**Last Updated:** 2026-05-22  
**Updates:** This FAQ is updated based on user questions
