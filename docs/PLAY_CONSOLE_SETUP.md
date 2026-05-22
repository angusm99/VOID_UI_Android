# Google Play Console Setup — Step by Step

**Goal:** Upload signed AAB and publish VOID UI to Play Store  
**Time:** ~30 minutes  
**Cost:** $25 one-time developer registration (if not already paid)

---

## PRE-SUBMISSION CHECKLIST

Before you start, confirm you have:

- [ ] Signed AAB file: `app-release.aab` (from Android Studio)
- [ ] Keystore file backed up (2 locations)
- [ ] Play Store assets:
  - [ ] Feature graphic (1024×500 PNG)
  - [ ] App icon (512×512 PNG)
  - [ ] Screenshots (6-8, 1440×3120 each)
- [ ] Privacy policy URL (GitHub Pages)
- [ ] Store listing copy (from PLAY_STORE_LISTING.md)

---

## Step 1: Go to Google Play Console

**URL:** https://play.google.com/console

Sign in with your Google account (angusm99@gmail.com)

---

## Step 2: Create a New App

If this is your first app:

1. Click **Create app** (blue button, top right)
2. **App name:** `VOID UI`
3. **Default language:** English
4. **App type:** **Application**
5. **Category:** **Personalization**
6. **Audience:** Not child-directed ✓
7. Click **Create app**

---

## Step 3: Fill in App Details

You're now in the app dashboard. On the left menu:

### 3a. App Access (Left menu → Settings → App access)

- Target audience: **Not child-directed** ✓
- Restricted content: None

### 3b. Audience & Content (Left menu → Setup → Target audience and content)

- Target audience: General
- Content rating: **Complete the rating questionnaire**
  - Click **Open questionnaire**
  - **Category:** Personalization
  - **Questions:**
    - Violence: None
    - Sexual content: None
    - Hate speech: None
    - Alcohol/tobacco: None
    - Gambling: None
    - Save answers
  - You should get rating: **Everyone (ESRB)**

### 3c: App Content (Left menu → Setup → App content)

- Contact email: `angusm99@gmail.com`
- Website: https://github.com/angusm99/VOID_UI_Android
- Emails for privacy/security issues: `angusm99@gmail.com`
- Phone number: (optional, leave blank)

---

## Step 4: Create App Release

On left menu → **Release** → **Production**

### 4a. Upload Signed AAB

1. Click **Create new release**
2. Under "App bundles," click **Upload**
3. Select your signed AAB:
   ```
   C:\Users\User\CLAUDE\VOID_UI_Android_Studio_Project\VOID_UI_Android\app\release\app-release.aab
   ```
4. Wait for upload and validation (30 seconds)
5. Check for errors (should say "Signed with upload key")

### 4b. Release Information

- **Release name:** v1.2 (or leave as auto-generated)
- **Release notes:**
```
VOID UI v1.2 — Premium Pack Expansion

✨ 568 new icons across 5 premium themed packs
✨ 32 variant icons for popular apps
✨ Samsung One UI full compatibility
✨ 856 total icons across all tiers

See store listing for full changelog.
```

Click **Save** (don't publish yet).

---

## Step 5: Add Store Listing

On left menu → **Store presence** → **Main store listing**

### 5a. Basic Info

| Field | Value |
|-------|-------|
| **App name** | VOID UI |
| **Short description** | (80 chars, from PLAY_STORE_LISTING.md) |
| **Full description** | (from PLAY_STORE_LISTING.md) |
| **App updates** | Leave as is |

### 5b: Graphic Assets

Click **Upload** for each:

| Asset | Dimensions | File |
|-------|-----------|------|
| **Feature graphic** | 1024×500 | Feature_Graphic.png |
| **Icon** | 512×512 | App_Icon_512.png |
| **Screenshots** | 1440×3120 | Screenshot_1.png, 2.png, etc. |

Upload 6-8 screenshots in order:
1. Feature showcase
2. Home screen mockup
3. Premium packs
4. Category showcase
5-8. Additional previews

Click **Save**.

---

## Step 6: Add Privacy Policy & Data Safety

On left menu → **Setup** → **App privacy**

### 6a. Privacy Policy

- **Privacy policy URL:**
```
https://angusm99.github.io/VOID_UI_Android/privacy-policy.md
```

Click **Save**.

### 6b. Data Safety (Left menu → Setup → Data safety)

Complete the data safety questionnaire:

**Question: Does your app collect or share user data?**
- Answer: **No**

**Question: Does your app use restricted permissions?**
- Answer: **No** (VOID UI requests zero permissions)

**Explanation:**
```
VOID UI is an icon pack that does not collect, store, transmit, or share 
any personal user data. No user authentication, no analytics, no advertising, 
no cookies, no tracking. Pure design asset with zero data handling.
```

Click **Save**.

---

## Step 7: Review All Settings

**Checklist before submission:**

- [ ] App name: VOID UI
- [ ] App type: Application
- [ ] Category: Personalization
- [ ] Target audience: Not child-directed
- [ ] Content rating: Everyone (ESRB)
- [ ] Signed AAB uploaded
- [ ] Feature graphic uploaded (1024×500)
- [ ] App icon uploaded (512×512)
- [ ] Screenshots uploaded (6-8)
- [ ] Short description filled (80 chars)
- [ ] Full description filled (2,847 chars)
- [ ] Release notes filled
- [ ] Privacy policy URL added
- [ ] Data safety form completed
- [ ] Contact email: angusm99@gmail.com

---

## Step 8: Choose Release Track

**Important:** First time submitting?

### Option A: Internal Testing (Recommended First)
- **Easier review process**
- **1-5 testers for 14 days**
- **Catch issues before production**

Steps:
1. Left menu → **Release** → **Testing** → **Internal testing**
2. Click **Create new release**
3. Upload same signed AAB
4. Add release notes
5. Click **Review release**
6. Click **Start rollout to internal testing**
7. Add testers (emails)
8. Submit

### Option B: Closed Testing
- **Larger beta group**
- **Up to 5,000 testers**
- **14-day minimum before production**

Steps:
1. Left menu → **Release** → **Testing** → **Closed testing**
2. Create track
3. Same upload process

### Option C: Production (Skip Beta)
- **Goes live immediately**
- **Higher risk if bugs exist**
- **Not recommended for first release**

**Recommendation:** Start with **Internal Testing** (1-2 testers, verify on real device, then promote to Production after 14 days).

---

## Step 9: Submit for Review

Once release track is set:

1. Click **Review release**
2. Check for errors (red warnings)
3. Click **Start rollout to [track]**

Play Store review begins (typically 24-48 hours for icon packs).

---

## Step 10: Monitor Review Status

Left menu → **Release** → **Your release track**

You'll see:
```
Status: In review
Review time: Usually 24-48 hours
```

Check back in 24 hours for approval.

---

## After Approval

### If Approved ✅

**For Internal Testing:**
- Wait 14 days (minimum)
- Monitor crash reports (should be zero)
- Check user feedback
- Then promote to Production

**For Production:**
- Goes live immediately
- Monitor Play Store reviews
- Check install stats in Analytics

### If Rejected ❌

- Google emails you the reason
- Common reasons for icon packs: none expected
- Fix issue and resubmit

---

## Important Notes

⚠️ **Keystore is tied to this app.** Every future update must use the same keystore and signing key. Don't lose it.

⚠️ **Version code only increases.** Next update must be versionCode 3 (not 2 again).

⚠️ **Package name is permanent.** Can't change `com.voidui.iconpack` without deleting and recreating.

⚠️ **Pricing is per-region.** When you add IAP, can set different prices per country.

---

## Links

- **Play Console:** https://play.google.com/console
- **Google Play Policies:** https://play.google.com/about/developer-content-policy/
- **App Bundle Format:** https://developer.android.com/guide/app-bundle

---

**Status:** Ready to follow  
**Last Updated:** 2026-05-22
