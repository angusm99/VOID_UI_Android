# Data Safety Form — Pre-filled Answers

**Play Store Requirement:** Every app must complete a data safety questionnaire  
**VOID UI Status:** Zero data collection, completes instantly

---

## Why This Form?

Google Play requires all apps to declare what data they collect. This protects users and ensures transparency. VOID UI's answer is simple: **we collect nothing**.

---

## Form Completion Guide

**Location in Play Console:**  
Left menu → **Setup** → **Data safety**

---

## Question 1: Does your app collect or share user data?

**Answer:** ❌ **No**

**Explanation:**
```
VOID UI is an icon pack that does not collect, store, transmit, 
or share any personal user data. No user authentication required. 
No analytics or crash reporting. No advertising or third-party 
tracking. Pure design asset with zero data handling.
```

---

## Question 2: What types of data does your app collect?

**Since you answered "No" to Q1:**  
This section is **automatically hidden**. You don't need to fill it.

---

## Question 3: Does your app use restricted permissions?

**Answer:** ❌ **No**

**Explanation:**
```
VOID UI requests zero permissions. The app does not access:
- Camera
- Microphone
- Contacts
- Location
- Calendar
- SMS/Phone
- Storage
- Sensors
- Or any other restricted resources

Icon packs are configured entirely in AndroidManifest.xml 
with launcher intent-filters. No runtime permissions needed.
```

---

## Question 4: What restricted permissions does your app use?

**Since you answered "No" to Q3:**  
This section is **automatically hidden**. You don't need to fill it.

---

## Save & Verify

1. Complete the form
2. Click **Save**
3. You should see:
   ```
   Data Safety Disclosure: Complete ✓
   
   Summary:
   - No user data collected
   - No restricted permissions
   - No third-party sharing
   ```

---

## Tip: Screenshots for Verification

If Google questions your submission:

**Evidence to include:**
- AndroidManifest.xml showing zero `<uses-permission>` tags
- app/build.gradle showing zero tracking/analytics libraries
- Privacy policy link (GitHub Pages)
- App description (icon pack only, no user data handling)

---

## Common Questions Google Might Ask

**Q: Is it normal for apps to collect zero data?**  
A: Yes, especially for icon packs, launcher themes, and design assets. These are purely graphical resources with no backend.

**Q: How does the app work without permissions?**  
A: Icon packs are configured via `AndroidManifest.xml` with launcher intent-filters. Launchers read the drawable resources directly without requiring app permissions.

**Q: Is this compliant with GDPR/CCPA?**  
A: Yes, VOID UI is fully compliant because it processes zero personal data.

---

## Form Status

**Estimated time to complete:** 2 minutes  
**Complexity:** Simple (zero data collection)  
**Approval risk:** Very low

---

## What Google Sees

When you submit:

**Public Data Safety Label (visible to users in Play Store):**
```
✓ This app doesn't collect or share any personal data

Data collected:
- No data collected

Data sharing:
- No data shared
```

**This builds user trust.** Users see your app is privacy-friendly.

---

## Save Form Answers

Copy-paste this into the form:

### Q1: Does your app collect or share user data?
```
No
```

### Explanation:
```
VOID UI is an icon pack that does not collect, store, transmit, or share 
any personal user data. No user authentication, analytics, advertising, or 
tracking. Pure design asset with zero data handling. Launchers access icon 
resources via standard Android APIs without requiring user data collection.
```

### Q3: Does your app use restricted permissions?
```
No
```

### Explanation:
```
VOID UI requests zero permissions. Icon packs are configured entirely in 
AndroidManifest.xml with launcher intent-filters. No runtime permissions needed. 
The app does not access camera, microphone, contacts, location, calendar, 
SMS, storage, sensors, or any restricted resources.
```

---

## Links

- **Play Console Data Safety Guide:** https://support.google.com/googleplay/android-developer/answer/10787469
- **Google Privacy Policy Requirements:** https://support.google.com/googleplay/answer/6014207
- **GDPR Compliance:** https://gdpr-info.eu/

---

**Status:** Ready to copy into Play Console  
**Completion time:** ~2 minutes  
**Approval probability:** 99% (zero-data apps always approved)
