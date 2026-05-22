# Keystore Backup & Recovery Guide

⚠️ **CRITICAL:** Your keystore is your identity on Google Play.  
**If lost, you can NEVER update VOID UI again.**

---

## What is a Keystore?

A keystore file (`.jks`) cryptographically signs your app bundle. It proves every update to VOID UI comes from you, not an attacker. Google Play ties your app to this keystore forever.

**Loss = permanent ban from updating that package.**

---

## Your Keystore Info

**File:** `VOID_UI.jks`  
**Location:** `C:\Users\User\VOID_UI.jks`  
**Size:** ~1-2 KB  
**Password:** [Your strong password]  
**Key Alias:** `void_ui_release`  
**Created:** 2026-05-22

---

## Backup Locations (2 Required)

### Location 1: USB Drive (Encrypted, Offline)

1. **Get a USB drive** (4GB or larger)
2. **Enable encryption** (BitLocker on Windows):
   - Right-click USB → Properties
   - Click "Enable BitLocker"
   - Set password (same as keystore password)
3. **Copy files:**
   ```
   USB:\VOID_UI_BACKUP\
   ├── VOID_UI.jks
   ├── KEYSTORE_PASSWORD.txt (encrypted, NOT in plaintext)
   ├── KEY_ALIAS.txt
   ├── CREATED_DATE.txt
   └── RECOVERY_INSTRUCTIONS.md
   ```
4. **Label clearly:** "VOID UI Keystore Backup — 2026-05-22"
5. **Store safely:** Locked drawer, safe, or safety deposit box

### Location 2: Cloud Storage (Encrypted)

**Option A: OneDrive (Microsoft account)**

1. Upload to private folder:
   ```
   OneDrive:\Private\VOID_UI_Keystore\
   ```
2. Ensure folder is "Personal" (not shared)
3. Note: OneDrive encrypts in transit + at rest

**Option B: Google Drive (Personal)**

1. Upload to private folder
2. Share with: No one
3. Verify: Only you can access

**Option C: iCloud Drive (Mac) or AWS S3 (more technical)**

Use if you prefer, but OneDrive/Google Drive are simplest.

⚠️ **DO NOT store password in cloud.** Store only the `.jks` file.

---

## File Organization

### What to Backup (Required)

```
VOID_UI.jks                   ← The keystore file (CRITICAL)
```

### What to Document (In Separate Secure Location)

Store **password** securely elsewhere:

**Option A: Password Manager (Recommended)**
- 1Password
- Bitwarden
- LastPass
- KeePass (offline)

**Option B: Encrypted Notes**
- OneNote with password
- Notion database (private)

**Option C: Written Record (Most Secure)**
- Write password on physical paper
- Store in safe or safety deposit box
- Separate from USB drive

**Never store password in:**
- Plaintext files on computer
- Email
- Cloud documents
- Shared folders
- GitHub or public repos

---

## Backup Checklist

Complete this before going to Play Store:

- [ ] Android Studio signed AAB build completed
- [ ] `VOID_UI.jks` exists at `C:\Users\User\VOID_UI.jks`
- [ ] Keystore password known and tested
- [ ] USB drive purchased and encrypted
- [ ] Keystore file copied to encrypted USB drive
- [ ] Cloud backup (OneDrive/Drive) contains `.jks` file
- [ ] Password stored in password manager (NOT in files)
- [ ] Backup locations tested (can you retrieve the file?)
- [ ] Backup tested in Android Studio (can you sign with it?)
- [ ] Both backup locations documented (folder paths, access methods)
- [ ] Recovery instructions written

---

## Testing Your Backups

### Test 1: USB Drive Recovery

1. Day after creating USB backup
2. Unplug USB, wait 1 hour
3. Plug it back in
4. Navigate to: `USB:\VOID_UI_BACKUP\`
5. Open `VOID_UI.jks` — confirm file exists and opens

### Test 2: Cloud Recovery

1. Log out of OneDrive/Google account
2. Log back in on different browser/incognito
3. Navigate to backup folder
4. Download `VOID_UI.jks`
5. Confirm file is intact (file size ~1-2 KB)

### Test 3: Signing with Recovered Keystore

**Before you need it**, test signing:

1. Android Studio → Build → Generate Signed Bundle
2. Point to your **cloud-downloaded copy** of `VOID_UI.jks`
3. Enter keystore password
4. Build succeeds → ✅ Backup is good

---

## Recovery Instructions (If Needed)

### Scenario: Lost Original Keystore

**Steps:**

1. **Retrieve from USB drive:**
   - Plug in encrypted USB
   - Enter BitLocker password
   - Copy `VOID_UI.jks` to:
     ```
     C:\Users\User\VOID_UI_RECOVERED.jks
     ```

2. **Or retrieve from cloud:**
   - Log into OneDrive/Google Drive
   - Navigate to backup folder
   - Download `VOID_UI.jks`
   - Save to:
     ```
     C:\Users\User\VOID_UI_RECOVERED.jks
     ```

3. **Sign next update with recovered keystore:**
   - Android Studio → Build → Generate Signed Bundle
   - Point to `VOID_UI_RECOVERED.jks`
   - Enter keystore password
   - Build new AAB

4. **Upload to Play Console:**
   - Same package name: `com.voidui.iconpack`
   - Next version code: 3 (or higher)
   - Submit normally

---

## Future Update Workflow

**Every time you update the app:**

1. Verify you have access to keystore:
   ```bash
   ls C:\Users\User\VOID_UI.jks
   ```

2. Build signed AAB with same keystore:
   - Android Studio → Build → Generate Signed Bundle
   - Use: `C:\Users\User\VOID_UI.jks`
   - Enter keystore password
   - Increment versionCode (2 → 3 → 4, etc.)

3. Upload to Play Console
4. Verify signing certificate matches (should say "Upload key" or "App signing key")

**⚠️ NEVER use a different keystore.**

---

## Warning Signs

**If any of these happen, contact Google Play support immediately:**

- [ ] Someone claims to have your keystore password
- [ ] You see an update from "VOID UI" you didn't publish
- [ ] Play Console shows signing certificate changed
- [ ] Malicious review: "This isn't the real icon pack"

**In these cases:**
- Email: support@google.com
- Explain keystore compromise
- Request app suspension while investigating

---

## Keystore Metadata

**Save this information securely (in password manager or paper):**

```
APP: VOID UI
PACKAGE: com.voidui.iconpack
KEYSTORE FILE: VOID_UI.jks
KEY ALIAS: void_ui_release
CREATED: 2026-05-22
VALIDITY: 25 years (expires 2051)
PASSWORD: [Your strong password]

BACKUP LOCATION 1: [USB drive, encrypted]
BACKUP LOCATION 2: [OneDrive/Google Drive folder]

TEST DATES:
- USB backup tested: [Date]
- Cloud backup tested: [Date]
- Signing test completed: [Date]
```

---

## Disaster Recovery Plan

If your hard drive crashes and you have NO keystore:

**Option 1: Restore from Backup (Best)**
- Retrieve from USB or cloud
- Rebuild app with same keystore
- Publish update normally
- **Cost:** None, **Time:** 1 hour

**Option 2: If NO Backup Exists (Catastrophic)**
- **You cannot update this app**
- Keystore is lost permanently
- Must create new package name: `com.voidui.iconpack.v2`
- Must republish entire app to Play Store
- Old app becomes "outdated" in user's library
- **Cost:** $25, **Time:** 3-5 days, **Damage:** User confusion

---

## Yearly Review

**Every December:**

- [ ] Test both backup locations still accessible
- [ ] Verify password manager still works
- [ ] Check USB drive still readable (USB degrades over 5-10 years)
- [ ] Refresh cloud backup (copy fresh file)
- [ ] Document test completion date
- [ ] Renew USB if older than 3 years

---

## Important Links

- **Android Signing Guide:** https://developer.android.com/studio/publish/app-signing
- **Play Console Signing:** https://support.google.com/googleplay/android-developer/answer/7384423
- **Keystore Recovery (if lost):** https://developer.android.com/studio/publish/app-signing#sign-bundle

---

## Summary

✅ **Do:**
- Store keystore in 2 places (USB + cloud)
- Encrypt USB with strong password
- Store password in password manager
- Test backups monthly
- Use same keystore forever

❌ **Don't:**
- Store password in plaintext files
- Share keystore with anyone
- Lose the file (you can't get it back)
- Use different keystore for updates
- Upload keystore to GitHub

---

**Status:** Action items for you  
**Urgency:** Complete before Play Store upload  
**Last Updated:** 2026-05-22
