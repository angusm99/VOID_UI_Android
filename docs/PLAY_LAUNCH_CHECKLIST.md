# VOID UI Play Store Launch Checklist

This file is the working handoff between Codex, Claude, Android Studio, and Play Console.

## Current Launch Goal

Ship VOID UI Icon Pack to Google Play as soon as possible with the lowest-risk release shape:

- Package: `com.voidui.iconpack`
- Version: `1.2`
- Version code: `2`
- Min SDK: `26`
- Target SDK: `35`
- Launch artifact: signed Android App Bundle (`.aab`)
- Initial monetization recommendation: launch free first, add paid/IAP structure in a later update after the base app is live.

## Build Status

Local project path:

`C:\Users\User\CLAUDE\VOID_UI_Android_Studio_Project\VOID_UI_Android`

Current status as of May 6, 2026:

- Debug APK build succeeded: `app/build/outputs/apk/debug/app-debug.apk`.
- Release bundle build succeeded: `app/build/outputs/bundle/release/app-release.aab`.
- The release AAB is unsigned and should be regenerated through Android Studio's signed bundle flow before upload.
- `app/src/main/res/drawable/` contains 856 VectorDrawable XML resources.
- `app/src/main/res/drawable-nodpi/` contains 733 VectorDrawable XML resources.
- Raw SVG files were converted to Android VectorDrawable XML because Android does not compile raw `.svg` files from `res/drawable/`.

Resolved blockers:

- Real Gradle wrapper JAR restored.
- Gradle wrapper bumped to Gradle 8.9 for Android Gradle Plugin 8.7.3.
- `local.properties` fixed locally to point at the installed Android SDK.
- `android.useAndroidX=true` added.
- Kotlin activities replaced with Java activities to avoid Kotlin Gradle setup.
- Android SDK Platform 35 is present locally.

## Why Target SDK 35

Google Play requires new apps and updates submitted after August 31, 2025 to target Android 15 / API level 35 or higher.

Source: https://developer.android.com/google/play/requirements/target-sdk

## Immediate Next Steps

1. Generate the signed release AAB in Android Studio.
2. Back up the keystore in at least two safe places.
3. Create the app in Play Console.
4. Add the privacy policy URL.
5. Complete App content declarations.
6. Upload the signed AAB to Closed testing.
7. Invite testers immediately if the account is subject to the 12-tester / 14-day rule.

## Signing Checklist

Use Android Studio:

1. **Build → Generate Signed Bundle / APK**.
2. Select **Android App Bundle**.
3. Create a new keystore if this is the first release.
4. Save the keystore somewhere permanent and backed up.
5. Build `release`.
6. Upload the signed `.aab` to Play Console.

Do not lose the keystore. Future updates to `com.voidui.iconpack` must be signed with the same app signing identity unless Google Play App Signing key upgrade flows are used.

## Play Console Requirements

### Testing Track

If the Play developer account is a personal account created after November 13, 2023, production access requires a closed test with at least 12 opted-in testers for 14 continuous days before applying for production.

Source: https://support.google.com/googleplay/android-developer/answer/14151465

Fast path:

1. Create the app in Play Console today.
2. Finish store setup enough to enable closed testing.
3. Upload signed `.aab` to Closed testing.
4. Invite at least 12 testers immediately.
5. Keep testers opted in for 14 continuous days.
6. Apply for production access as soon as the requirement is satisfied.

### App Content

Complete these in Play Console:

- Privacy policy URL: `https://github.com/angusm99/VOID_UI_Android/blob/master/docs/privacy-policy.md`
- Data safety form: no user data collected or shared.
- Ads declaration: `No`, unless ads are added later.
- App access: no restricted login required.
- Target audience/content: general users, not child-directed.
- Content rating questionnaire.
- News app declaration: `No`.
- Government app declaration: `No`.
- Financial features declaration: `No`.

Google requires Data safety declarations for apps published on testing or production tracks. Apps that collect no user data still need to complete the form and provide a privacy policy.

Sources:

- https://support.google.com/googleplay/android-developer/answer/10787469
- https://support.google.com/googleplay/android-developer/answer/9888076
- https://support.google.com/googleplay/android-developer/answer/9859455

## Store Listing Draft

### App Name

VOID UI Icon Pack

### Short Description

Minimal AMOLED icon pack with 856 black-and-white monoline icons.

### Full Description

VOID UI is a minimalist AMOLED icon pack for Android launchers. It uses pure black backgrounds, crisp white monoline strokes, and a premium editorial visual style designed for dark homescreens.

Includes:

- 856 launcher-ready icons
- Core VOID UI app icons
- AI, social, productivity, media, finance, system, developer, travel, and lifestyle icons
- Premium-style themed sets including Circuitry, Terminal, Sports Zones, Cricket Nations, and Xenocomm
- Compatibility-focused app mappings for popular launchers

Works with supported third-party launchers such as Nova, Niagara, Apex, Action, Lawnchair, ADW, and other launchers that support standard icon pack mappings.

How to apply:

1. Install VOID UI Icon Pack.
2. Open your launcher settings.
3. Find Icon Pack or Themes.
4. Select VOID UI.

VOID UI does not collect or share user data.

### Release Notes

VOID UI 1.2 expands the pack to 856 icons, updates premium themed sets, adds Xenocomm icons, refreshes app metadata, converts icon resources to Android VectorDrawable XML, and targets SDK 35 for Google Play.

## Asset Checklist

Required before store submission:

- App icon: existing launcher icon present in `mipmap-*`.
- Feature graphic: 1024 x 500 PNG/JPG.
- Phone screenshots: at least 2, preferably 6-8.
- Optional tablet screenshots if claiming tablet support.
- Promo copy and category.
- Contact email.
- Privacy policy public URL.

Recommended screenshots:

1. Dark homescreen preview with VOID UI applied.
2. Icon grid on pure black background.
3. AI icons group.
4. Circuitry pack preview.
5. Terminal pack preview.
6. Xenocomm pack preview.

## Recommended First Release Scope

For speed, do not add billing/IAP before first Play submission. Billing adds SDK setup, product setup, purchase restore flows, policy surface, and review risk. Launch the full pack first as free or paid. Add freemium/IAP gating only after the first release path is stable.
