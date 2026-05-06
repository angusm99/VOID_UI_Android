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

## Why Target SDK 35

Google Play requires new apps and updates submitted after August 31, 2025 to target Android 15 / API level 35 or higher.

Source: https://developer.android.com/google/play/requirements/target-sdk

## Build Blockers Found Locally

Local project path:

`C:\Users\User\CLAUDE\VOID_UI_Android_Studio_Project\VOID_UI_Android`

Current local blockers:

1. `JAVA_HOME` is not set and `java` is not on PATH.
2. Android Studio's bundled JDK exists at `C:\Program Files\Android\Android Studio\jbr`.
3. `local.properties` still contains `sdk.dir=/path/to/your/Android/Sdk`.
4. No normal Android SDK install was found under `C:\Users\User\AppData\Local\Android\Sdk`.
5. `gradle/wrapper/gradle-wrapper.jar` is a 201-byte placeholder, so `gradlew.bat` fails with `ClassNotFoundException: org.gradle.wrapper.GradleWrapperMain`.
6. The old Kotlin activity files were present but the Gradle project had no Kotlin plugin. The launch-prep branch replaces them with Java activities.

## Android Studio Fix Path

Do this once on the machine that will build the signed release:

1. Open Android Studio.
2. Install Android SDK Platform 35 and matching build tools from SDK Manager.
3. Open the project folder.
4. Let Android Studio repair/update the Gradle wrapper if prompted.
5. Confirm `local.properties` points to the real SDK, usually `C:\Users\User\AppData\Local\Android\Sdk`.
6. Sync Gradle.
7. Build an unsigned debug APK first.
8. Generate the signed Android App Bundle.

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

- Privacy policy URL.
- Data safety form.
- Ads declaration: likely `No`, unless ads are added.
- App access: no restricted login required.
- Target audience/content: likely adults/general users, not child-directed.
- Content rating questionnaire.
- News app declaration: `No`.
- Government app declaration: `No`.
- Financial features declaration: `No`, unless the app offers financial services.

Google requires Data safety declarations for apps published on testing or production tracks. Apps that collect no user data still need to complete the form and provide a privacy policy.

Sources:

- https://support.google.com/googleplay/android-developer/answer/10787469
- https://support.google.com/googleplay/android-developer/answer/9888076
- https://support.google.com/googleplay/android-developer/answer/9859455

## Privacy Policy Draft

Use this as the basis for a public webpage, not a PDF.

Title: Privacy Policy for VOID UI Icon Pack

VOID UI Icon Pack does not collect, store, sell, or share personal user data. The app is an Android icon pack used by compatible launchers to apply custom icons. It does not require an account, does not include ads, does not use analytics, and does not transmit user data to the developer or third parties.

The app may be distributed through Google Play, which may collect information according to Google's own policies. Those Google Play practices are controlled by Google, not by VOID UI Icon Pack.

Privacy contact: [add developer contact email]

Last updated: [add date]

## Store Listing Draft

### App Name

VOID UI Icon Pack

### Short Description

Minimal AMOLED icon pack with 856 black-and-white monoline icons.

### Full Description

VOID UI is a minimalist AMOLED icon pack for Android launchers. It uses pure black backgrounds, crisp white monoline strokes, and a premium editorial visual style designed for dark homescreens.

Includes:

- 856 launcher-ready SVG icons
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

VOID UI 1.2 expands the pack to 856 icons, updates premium themed sets, adds Xenocomm icons, refreshes app metadata, and prepares the project for Google Play target SDK 35.

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

## Codex Branch

Launch-prep branch:

`codex/play-launch-prep`

Changes on this branch:

- Target SDK raised to 35.
- Version updated to 1.2 / versionCode 2.
- App metadata updated from 197/164 icons to 856 icons.
- Kotlin activities replaced with Java activities to avoid requiring Kotlin Gradle setup.
- In-app privacy statement added.
- README on master was already updated with the expanded icon library overview.
