# VOID UI — Minimalist Android Icon Pack

![Version](https://img.shields.io/badge/version-1.8-black)
![Android](https://img.shields.io/badge/Android-8.0%2B-black)
![Icons](https://img.shields.io/badge/icons-856-black)
![License](https://img.shields.io/badge/license-MIT-black)
![Privacy](https://img.shields.io/badge/data-zero%20collection-success)

> **Pure black. Pure white. Pure design.**

Minimalist AMOLED icon pack for Android with 856 icons across 6 themed packs. Designed for users who value premium minimalism, privacy, and battery efficiency.

---

## Quick Facts

| Field | Detail |
|---|---|
| **Package** | `com.voidui.iconpack` |
| **Version** | 1.8 (versionCode 8) |
| **Min SDK** | 26 (Android 8.0+) |
| **Target SDK** | 35 (Android 15) |
| **Icons** | **856** Android VectorDrawable XMLs |
| **Premium Packs** | 5 themed packs (568 icons) |
| **Privacy** | Zero data collection ✅ |
| **Permissions** | None required ✅ |
| **Launchers** | 9 supported ✅ |

---

## Get VOID UI

📱 **[Install from Google Play Store](https://play.google.com/store/apps/details?id=com.voidui.iconpack)**

🛠️ **[View Source on GitHub](https://github.com/angusm99/VOID_UI_Android)**

🎨 **[Design Files on Figma](https://www.figma.com/design/4kszGYksUUIETAxL7mcXvM)**

---

## What's Included

### Free Tier (288 Icons)

Comprehensive branded icons covering 14 categories:

- 🤖 **AI & Models** (Claude, ChatGPT, Gemini, Grok, Copilot + more)
- 💬 **Social & Messaging** (Instagram, TikTok, Twitter, Discord, etc.)
- 📧 **Email & Inbox** (Gmail, Outlook + variants)
- 💼 **Productivity** (Notion, Slack, Office, Google Workspace)
- 🎵 **Media** (Spotify, YouTube, Netflix, Apple Music + more)
- 💰 **Finance** (PayPal, Crypto, Stripe, Amazon + more)
- 💻 **Tech** (AWS, GitHub, Docker, Kubernetes + more)
- 🗺️ **Navigation** (System controls, gestures)
- 📁 **Files** (Drive, Dropbox, cloud services)
- 🚗 **Travel** (Maps, Uber, Airbnb, Waze + more)
- 🏃 **Health** (Fitness, meditation, wellness)
- 👥 **People** (Contacts, authentication, VPN, privacy)
- ☀️ **Weather** (Climate, seasonal apps)
- 🛠️ **Tools** (System utilities, miscellaneous)

### Premium Packs (568 Icons — In-App Purchase)

5 themed icon packs with distinct aesthetics:

#### 🌐 CIRCUITRY (94 icons)
*Neon circuit board aesthetic*
- Glowing matrix green endpoints
- 14px round stroke, terminal dots at line endings
- Default accent: `#00FF41`
- Perfect for: Tech enthusiasts, developers

#### 📺 TERMINAL (108 icons)
*Retro amber CRT phosphor glow*
- Amber `#FFB000` on black
- 90° corners, no rounded line caps
- Double CRT line effect with phosphor blur
- Perfect for: Retro/cyberpunk fans, terminal lovers

#### 👽 XENOCOMM (123 icons)
*Alien bioluminescent sci-fi*
- Cyan `#00FFE5` + violet `#9D4EDD`
- Organic curves mixed with crystalline geometry
- Perfect for: Sci-fi fans, futuristic aesthetic

#### 🏏 CRICKET NATIONS (16 icons)
*Geometric nation symbolism*
- Abstract nation cricket representations
- All major cricket-playing nations included
- Perfect for: Cricket fans, regional users

#### ⚽ SPORTS ZONES (30 icons)
*Runtime colour-adaptive team icons*
- Dynamic colour substitution via `ZONE_PRIMARY/SECONDARY/ACCENT`
- 1,000+ possible team colour combinations
- Perfect for: Sports fans, fantasy league users

---

## Features

### 🖤 AMOLED-First Design
Pure black backgrounds (`#000000`) optimize battery on AMOLED screens. White monoline strokes contrast crisply against black.

### 🎯 Pixel-Perfect Grid
All icons follow a consistent 108×108dp grid with 1:1 pixel alignment. Scales beautifully on any DPI density.

### 🔐 Privacy-First
- Zero data collection
- No analytics or tracking
- No third-party SDKs
- No permissions required
- No account needed

### 🚀 Launcher Compatible

| Launcher | Status |
|----------|--------|
| Nova Launcher | ✅ Native |
| Niagara Launcher | ✅ Native |
| Apex Launcher | ✅ Native |
| Action Launcher | ✅ Native |
| ADW Launcher | ✅ Native |
| Lawnchair | ✅ Native |
| Atom Launcher | ✅ Native |
| Tesla Launcher | ✅ Native |
| **Samsung One UI** | ✅ Native |

### 🎨 Accent Colour Variants (Planned for v1.4)
Each premium pack will support 5 accent variants:
- **Cyber** (Neon blue)
- **Neon** (Bright green)
- **Ultra** (Vivid pink)
- **Pulse** (Electric purple)
- **Blaze** (Blazing orange)

---

## Documentation

Full project documentation in `docs/`:

| File | Purpose |
|------|---------|
| [ICON_INVENTORY.md](docs/ICON_INVENTORY.md) | All 856 icons categorized by tier |
| [PLAY_STORE_LISTING.md](docs/PLAY_STORE_LISTING.md) | Play Store copy & assets |
| [PLAY_CONSOLE_SETUP.md](docs/PLAY_CONSOLE_SETUP.md) | Console upload guide |
| [DATA_SAFETY_FORM.md](docs/DATA_SAFETY_FORM.md) | Pre-filled questionnaire |
| [PRIVACY_POLICY_HOSTING.md](docs/PRIVACY_POLICY_HOSTING.md) | GitHub Pages setup |
| [KEYSTORE_BACKUP.md](docs/KEYSTORE_BACKUP.md) | Critical backup procedures |
| [POST_LAUNCH_PLAN.md](docs/POST_LAUNCH_PLAN.md) | 90-day post-launch plan |
| [LAUNCH_MARKETING.md](docs/LAUNCH_MARKETING.md) | Launch day templates |
| [IAP_IMPLEMENTATION_GUIDE.md](docs/IAP_IMPLEMENTATION_GUIDE.md) | Premium packs setup |
| [V1_3_ROADMAP.md](docs/V1_3_ROADMAP.md) | Future development plan |
| [FAQ.md](docs/FAQ.md) | Frequently asked questions |
| [privacy-policy.md](docs/privacy-policy.md) | Privacy policy (public URL) |

---

## Building from Source

### Prerequisites
- Android Studio (latest stable)
- JDK 17+
- Android SDK 35
- Gradle 8.9

### Setup

1. Clone this repository:
```bash
git clone https://github.com/angusm99/VOID_UI_Android.git
cd VOID_UI_Android
```

2. Open in Android Studio:
   - File → Open → Select the `VOID_UI_Android` folder
   - Wait for Gradle sync to complete

3. Build:
```bash
# Debug APK (sideload testing)
./gradlew assembleDebug

# Release AAB (Play Store)
./gradlew bundleRelease
```

### Signing
For Play Store submission, you need a release keystore:
- **Build → Generate Signed Bundle / APK**
- Follow the wizard to create a new keystore
- **CRITICAL:** Backup the keystore in 2 safe locations

---

## Project Structure

```
VOID_UI_Android/
├── app/
│   ├── src/main/
│   │   ├── AndroidManifest.xml         Launcher intent filters
│   │   ├── java/com/voidui/iconpack/
│   │   │   ├── MainActivity.java       App entry
│   │   │   └── IconPackActivity.java   Launcher entry point
│   │   └── res/
│   │       ├── drawable/              856 VectorDrawable XMLs
│   │       ├── drawable-nodpi/        733 additional VectorDrawables
│   │       ├── xml/appfilter.xml      Launcher icon mappings (200+)
│   │       ├── mipmap-*/              Launcher icon PNGs
│   │       └── values/                Strings, styles, colors
│   └── build.gradle                   Build configuration
├── docs/                              Comprehensive documentation
├── gradle/wrapper/                    Gradle 8.9 wrapper
├── build.gradle                       Root build config
└── settings.gradle                    Module configuration
```

---

## Contributing

Contributions welcome! See our [Issues page](https://github.com/angusm99/VOID_UI_Android/issues):

- 🐛 **[Report a bug](https://github.com/angusm99/VOID_UI_Android/issues/new?template=bug_report.md)**
- 💡 **[Request a feature](https://github.com/angusm99/VOID_UI_Android/issues/new?template=feature_request.md)**
- 🎨 **[Request an icon](https://github.com/angusm99/VOID_UI_Android/issues/new?template=missing_icon.md)**

### Code Contributions

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

MIT License — see [LICENSE](LICENSE) file for details.

Icons (SVG files in `ICON MASTER/`) are Creative Commons CC-BY 4.0.

---

## Acknowledgments

- **svg2vectordrawable** — for SVG → VectorDrawable conversion
- **Material Icons** — design inspiration for some categories
- **r/androidthemes** community — for invaluable feedback
- **Beta testers** — for testing early versions

---

## Contact

**Maker:** Angus M.  
**Email:** angusm99@gmail.com  
**GitHub:** [@angusm99](https://github.com/angusm99)  
**Location:** Cape Town, South Africa

For questions, suggestions, or just to say hi — drop me a message!

---

<p align="center">
  <strong>VOID UI</strong><br>
  Pure black. Pure white. Pure design. 🖤
</p>
