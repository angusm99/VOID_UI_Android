# VOID UI Icon Pack — HANDOFF

Self-contained brief so any AI/dev can continue cold. Updated: 2026-07-05 (v1.9.8).

## What this is
Minimalist AMOLED icon pack for Android. Pure black backgrounds, white monoline
strokes (uniform **14px effective** at 512 viewport), premium themed packs, and
a runtime colour-tint gallery. Owner: Angus Martin (angusm99). SA/British English.

## State right now
- **v1.9.8 (versionCode 20)**, commit `8a770ad`, working tree clean, pushed.
- Debug APK: `app/build/outputs/apk/debug/app-debug.apk` (5.9 MB).
- **811 VectorDrawables** in `res/drawable-nodpi/` — the ONLY icon dir
  (`res/drawable/` was a byte-identical duplicate, deleted in v1.9.8; all
  scripts repointed — do NOT recreate it).
- appfilter.xml ×3 (res/xml, res/raw, assets) are **byte-identical, 375 entries**,
  all resolving to real drawables. Keep them in sync — edit one, copy to all.
- Test device: "Rural Juror" Samsung S21 Ultra via ADB wireless
  (`adb mdns services` → connect; pairing already done from this PC).
  Wireless debugging drops when the screen locks; IP hops between .41/.162.

## Build (command line, no Android Studio needed)
```bash
export JAVA_HOME="/c/Program Files/Android/Android Studio/jbr"
cd VOID_UI_Android && ./gradlew assembleDebug
# install: adb install -r app/build/outputs/apk/debug/app-debug.apk
```

## Architecture
- `MainActivity.java` — entire gallery UI built in code (no layouts). Search,
  category chips, 6 neon tint presets + custom RGB picker. Tint persists via
  SharedPreferences `void_ui_prefs/icon_tint`; applied with
  `setColorFilter(SRC_IN)`, **cleared at white** so baked colours show.
- `IconPackActivity.java` — Theme.NoDisplay stub that satisfies launcher
  icon-pack intents (Nova/ADW/Apex/Action/Niagara/Smart/GO) then finishes.
- Icon list comes from `values/icon_pack.xml` — two **index-aligned parallel
  arrays** (`icon_pack_drawables`, `icon_pack_names`). Trim them together.
- `res/xml/drawable.xml` — launcher icon-picker list (811 entries).
- Launcher app-mapping: `appfilter.xml` (+ `assets/appmap.xml`,
  `assets/theme_resources.xml` for some launchers).

## Icon rules (hard-won, don't regress)
1. **No opaque background plates** in any drawable — `SRC_IN` tint paints them
   solid and the icon becomes a square. Gallery/launcher supply the black.
2. **14px effective stroke** everywhere (Circuitry's weight): raw strokeWidth ×
   group-scale ÷ viewport × 512 ≈ 14. `scripts/normalize_stroke_weight.py`
   enforces this; idempotent.
3. Xeno + Terminal art is **generated** — placeholders were 121/123 and 105/108
   byte-identical. `generate_xeno_mono.py` (shared engine, prefix-aware) +
   `generate_terminal_mono.py` rebuild them: hand-authored GLYPHS dict + core
   glyph recolouring. Edit the GLYPHS dict to change art, then re-run.
4. Sports Zones SVGs use ZONE_PRIMARY/SECONDARY/ACCENT placeholders
   (see `regenerate_master_svg_vectors.py` COLOR_MAP).

## Masters
`C:\Users\User\CLAUDE\VOID_UI\01_ICON_PACK_MASTER\ICON_MASTER\` — 9 series of
source SVGs. The 4 `VOID_UI_OPEN_DESIGN_TRANSFER` folders scattered around are
**stale duplicates** (pre-v1.9.x placeholders) — do not source from them.

## Next steps (in order)
1. Generate signed release AAB (needs Android Studio: Build → Generate Signed
   Bundle; keystore per docs/KEYSTORE_BACKUP.md).
2. Host privacy policy (GitHub Pages from docs/privacy-policy.md).
3. Play Console: upload AAB to testing track; listing copy in
   docs/PLAY_STORE_LISTING.md; data safety in docs/DATA_SAFETY_FORM.md.
4. Optional polish: some `_v` brand variants are weak marks (chatgpt_v4 is a
   generic sparkle, chatgpt_v5 a rounded square) — audit or cut before launch.
5. Back up 01_ICON_PACK_MASTER to git/cloud (currently local-only).
