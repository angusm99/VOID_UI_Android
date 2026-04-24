# VOID UI — Android Icon Pack

Minimalist AMOLED icon pack. 197 icons. Pure black. White strokes.

---

## Opening in Android Studio

1. **File → Open** → select this `VOID_UI_Android` folder
2. When prompted about the Gradle wrapper, click **"Update Gradle wrapper"** — Android Studio will download the correct `gradle-wrapper.jar` automatically (the stub included here is a placeholder)
3. Let Gradle sync complete (~1–2 min on first run, requires internet)
4. Done — project is ready to build

> **Note:** `local.properties` → update `sdk.dir` to your local Android SDK path if Android Studio doesn't set it automatically (it usually does).

---

## Building the APK / AAB

### For Play Store (recommended — AAB):
**Build → Generate Signed Bundle / APK → Android App Bundle**

### For sideloading / testing (APK):
**Build → Generate Signed Bundle / APK → APK**

You'll need to create a **keystore** on first signed build. Android Studio walks you through it. **Keep your keystore file safe** — you need it for every future update.

---

## Project Structure

```
app/src/main/
  AndroidManifest.xml          — launcher intent-filters (Nova, Niagara, Apex, Action, Lawnchair, ADW)
  java/com/voidui/iconpack/
    MainActivity.kt            — app entry screen
    IconPackActivity.kt        — launcher entry point
  res/
    drawable/ + drawable-nodpi/  — 197 SVG icons (164 core + 33 variants)
    xml/appfilter.xml            — 86 app → icon mappings
    mipmap-*/                    — launcher icon PNGs (all densities)
    layout/activity_main.xml
    values/strings.xml + styles.xml
```

---

## Colour Variants

Five additional colour packs are ready in `VOID_UI_CORE_PACKS/`:
- cyan (#00FFFF), green (#39FF14), purple (#BF00FF), pink (#FF007F), amber (#FF9500)

Each needs its own Android project with a unique package name:
- `com.voidui.iconpack.cyan`
- `com.voidui.iconpack.green`
- etc.

---

## Package: `com.voidui.iconpack`
## Version: 1.0 (versionCode 1)
## Min SDK: 26 (Android 8.0)
## Target SDK: 34
