# VOID UI — Android Icon Pack

Minimalist AMOLED icon pack for Android. Pure black backgrounds, white monoline strokes. Clean, premium, editorial aesthetic.

---

## Overview

| Field | Detail |
|---|---|
| Package | `com.voidui.iconpack` |
| Version | 1.2 |
| Min SDK | 26 (Android 8.0) |
| Target SDK | 35 |
| Drawables | **856 Android VectorDrawable XML files** in `app/src/main/res/drawable/` |
| Master Library | **1,394 SVGs** across 9 series in ICON MASTER |
| GitHub | [angusm99/VOID_UI_Android](https://github.com/angusm99/VOID_UI_Android) |
| Figma | [VOID UI — Icon Pack](https://www.figma.com/design/4kszGYksUUIETAxL7mcXvM) |
| Privacy Policy | [docs/privacy-policy.md](docs/privacy-policy.md) |

---

## Opening in Android Studio

1. **File → Open** → select this `VOID_UI_Android` folder.
2. Let Gradle sync complete. The first sync usually takes 1-2 minutes and requires internet access.
3. Build from Android Studio once sync has completed.

> **Note:** If Android Studio does not set it automatically, update `local.properties` with your local Android SDK path.

---

## Building the APK / AAB

### Play Store build

Use **Build → Generate Signed Bundle / APK → Android App Bundle**.

### Sideloading / testing build

Use **Build → Generate Signed Bundle / APK → APK**.

You will need to create a keystore for the first signed build. Keep the keystore file safe because every future update must be signed with the same key.

---

## Project Structure

```text
app/src/main/
  AndroidManifest.xml            Launcher intent filters
  java/com/voidui/iconpack/
    MainActivity.java            App entry screen
    IconPackActivity.java        Launcher entry point
  res/
    drawable/                    856 VectorDrawable icon resources
    drawable-nodpi/              733 VectorDrawable icon resources
    xml/appfilter.xml            App-to-icon mappings
    mipmap-*/                    Launcher icon PNGs
    layout/activity_main.xml
    values/strings.xml
    values/styles.xml
```

---

## ICON MASTER Structure

| Folder | Series | Count | Prefix | Tier |
|---|---|---:|---|---|
| `01_APP_ICONS/` | Framed + bare app icons | 188 | `ic_` | Free |
| `02_VOID_UI/` | Monoline system icons, AI brands, phone variants | 195 | various | Free |
| `03_MANUS_CIRCUIT/` | Neon circuit line icons | 210 | numbered | Premium |
| `04_SYSTEM_UICONS/` | General system/UI icons | 430 | names | Internal |
| `05_CIRCUITRY/` | PCB circuit-board aesthetic | 94 | `circuitry_` | Premium |
| `06_TERMINAL/` | CRT amber terminal style | 108 | `terminal_` | Premium |
| `07_CRICKET_NATIONS/` | Abstract cricket nation symbols | 16 | `nation_` | Premium add-on |
| `08_SPORTS_ZONES/` | Runtime colour-zone sports icons | 30 | `sports_` | Premium add-on |
| `09_XENOCOMM/` | Alien worlds comms icons | 123 | `xeno_` | Premium |

---

## Android Drawable Contents

| Prefix | Pack | Count |
|---|---|---:|
| `ic_` | Core VOID UI app icons | 94 |
| `circuitry_` | Circuitry premium pack | 94 |
| `terminal_` | Terminal CRT pack | 108 |
| `nation_` | Cricket Nations add-on | 16 |
| `sports_` | Sports Zones add-on | 30 |
| `xeno_` | Xenocomm premium pack | 123 |
| various | Variant icons, including Claude and ChatGPT versions | ~391 |
| **Total** |  | **856** |

---

## Freemium Model

| Tier | Content | Price |
|---|---|---|
| Free | Core VOID UI app icons | Free |
| Premium | Circuitry pack | IAP |
| Premium | Terminal pack | IAP |
| Premium | Sports Zones | IAP |
| Premium | Cricket Nations | IAP |
| Premium | Xenocomm pack | IAP |

Accent colour variants are planned at pack level: Cyber, Neon, Ultra, Pulse, and Blaze.

---

## Premium Pack Design Rules

### Circuitry

- Stroke: `strokeWidth="14"`, `strokeLinecap="round"`.
- Terminal dots: filled circles with `r="9"` at line endpoints.
- Default accent: matrix green `#00FF41`.

### Terminal

- Amber `#FFB000` on black.
- 90-degree corners with no rounded line caps.
- Double CRT line effect: two parallel strokes, with the second at 40% opacity.
- Phosphor glow via SVG `<filter>` with `feGaussianBlur stdDeviation="3"`.

### Sports Zones

Runtime colour placeholders in SVG paths:

| Placeholder | Usage |
|---|---|
| `ZONE_PRIMARY` | Team primary colour |
| `ZONE_SECONDARY` | Team secondary colour |
| `ZONE_ACCENT` | Highlight or trim colour |

### Xenocomm

- Bioluminescent cyan `#00FFE5` and violet `#9D4EDD`.
- Organic flowing curves mixed with crystalline geometry.

---

## Figma

| Page | Contents |
|---|---|
| Page 1 | 291 VOID UI core icons grouped by category on black backgrounds |
| Manus — Circuit Line Icons | 200 circuit line icons |

### Page 1 Categories

| Category | Count |
|---|---:|
| AI & Models | ~45 |
| Social & Messaging | ~25 |
| Productivity & Work | ~35 |
| Media & Entertainment | ~22 |
| Finance & Commerce | ~19 |
| Tech & Connectivity | ~20 |
| Navigation & UI | ~45 |
| Files & Storage | ~8 |
| Maps & Travel | ~10 |
| Health & Lifestyle | ~12 |
| People & Security | ~16 |
| Uncategorised | ~12 |

---

## Colour Variants

| Pack | Package | Colour |
|---|---|---|
| Cyan | `com.voidui.iconpack.cyan` | `#00FFFF` |
| Green | `com.voidui.iconpack.green` | `#39FF14` |
| Purple | `com.voidui.iconpack.purple` | `#BF00FF` |
| Pink | `com.voidui.iconpack.pink` | `#FF007F` |
| Amber | `com.voidui.iconpack.amber` | `#FF9500` |
