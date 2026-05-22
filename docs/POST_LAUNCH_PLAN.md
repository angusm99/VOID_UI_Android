# Post-Launch Action Plan

**Phase:** After VOID UI goes live on Google Play  
**Duration:** First 30 days critical, 90 days full monitoring

---

## Phase 1: Launch Day (Day 0)

### Immediate Actions

- [ ] Verify app appears in Play Store search (may take 1-4 hours)
- [ ] Install on your own device via Play Store (test real install flow)
- [ ] Verify icon pack applies correctly to Nova Launcher
- [ ] Verify icon pack applies to Samsung One UI launcher
- [ ] Check for any crashes (shouldn't be any)
- [ ] Confirm privacy policy URL loads from store listing

### Testing Checklist

| Test | Expected Result | Status |
|------|-----------------|--------|
| App installs from Play Store | No errors | __ |
| App launches without crash | Instant open | __ |
| Nova Launcher can detect pack | Shows in themes | __ |
| Niagara Launcher applies icons | All icons theme | __ |
| Samsung launcher applies pack | Galaxy icons themed | __ |
| Uninstall works cleanly | No leftover files | __ |

### Initial Promotion

- [ ] Post on Reddit: r/androidthemes (with screenshots)
- [ ] Post on Reddit: r/androidapps (mention free tier)
- [ ] GitHub README link to Play Store
- [ ] Share with design communities (if applicable)

---

## Phase 2: First Week (Days 1-7)

### Daily Monitoring

Each day, check Play Console:

**Left menu → Analytics**

- [ ] **Installs:** Monitor daily count (expect 10-100 first week)
- [ ] **Crashes:** Should be **0**. If any crashes → check crash reports immediately
- [ ] **ANRs** (app not responding): Should be **0**
- [ ] **Ratings:** Check for 5★ and 1★ reviews (read feedback)
- [ ] **Retention:** % of users who keep after 1 day

**Left menu → Reviews**

- [ ] Read every review (should be few initially)
- [ ] Reply to 5★ reviews: "Thanks for using VOID UI!"
- [ ] Reply to negative reviews: Investigate issue, offer fix
- [ ] Look for missing app icon requests

### Crash Reports

If any crashes appear:

1. Click crash in Play Console
2. Read stack trace
3. Check if it's device-specific (e.g., only on Android 8)
4. Fix in code if needed
5. Build new APK, upload v1.2.1 (versionCode 3)
6. Publish to Play Store

---

## Phase 3: First Month (Days 1-30)

### Weekly Tasks

**Every Monday:**

- [ ] Check analytics dashboard
  - Installs (trend up?)
  - Crash rate (should stay 0%)
  - Uninstall rate (track churn)
  - Rating average (aim for 4.5+)
- [ ] Read & reply to reviews
- [ ] Check GitHub issues for feature requests

**Every Wednesday:**

- [ ] Monitor Play Store listing engagement
  - Click-through rate (visitors who install)
  - Impressions vs. installs
  - Device/OS breakdown (which devices use most?)

**Every Friday:**

- [ ] Analyze user feedback trends
  - Recurring feature requests?
  - Missing app icons?
  - Performance complaints?
  - Design feedback?

### 30-Day Goals

- [ ] Reach 100+ installs
- [ ] Maintain 0% crash rate
- [ ] Achieve 4.0+ star rating
- [ ] Document top 5 feature requests
- [ ] Fix any critical bugs

---

## Phase 4: Second Month (Days 30-60)

### Feature Planning

Based on month 1 feedback:

- [ ] Identify 3 most-requested app icons
- [ ] Design 10-15 new icons based on user feedback
- [ ] Plan v1.3 update with new icons
- [ ] Draft update announcement

### Optimization

- [ ] Update store listing description based on clicks/installs
  - If click rate is low (<10%), description needs improvement
  - Update screenshots if needed
- [ ] Add new screenshots if device variety improves (tablet, fold, etc.)
- [ ] Consider A/B testing store listing (Google Play experiments)

### IAP Planning

Prepare for premium pack launch:

- [ ] Finalize IAP pricing (recommend $0.99-$2.99 per pack)
- [ ] Draft store descriptions for each premium pack
- [ ] Plan marketing (which pack to launch first?)
- [ ] Test IAP flow locally before uploading

---

## Phase 5: Third Month (Days 60-90)

### Analytics Review

Compile 90-day report:

- [ ] Total installs: ___
- [ ] Average rating: ___
- [ ] Crash rate: ___
- [ ] Retention rate (1-day, 7-day, 30-day): ___, ___, ___
- [ ] Top devices: ___, ___, ___
- [ ] Top locations: ___, ___, ___

### Major Milestone: Premium Pack Launch

- [ ] Publish v1.3 with new icons
- [ ] Launch 1st premium pack as IAP (recommend CIRCUITRY)
- [ ] Monitor IAP conversion rate (% who purchase)
- [ ] Adjust pricing if needed (if <1% convert, lower price)

### Community Engagement

- [ ] Read all user reviews (document sentiment)
- [ ] Implement top 3 requested features in v1.4
- [ ] Plan release schedule (bi-weekly updates?)

---

## Ongoing Metrics to Track

**Health Indicators:**

| Metric | Healthy Range | Danger Zone |
|--------|---------------|------------|
| Crash Rate | 0.0% | >0.1% |
| Rating | 4.0★+ | <3.5★ |
| Installs/day | >5 | <1 |
| Retention (1-day) | >70% | <50% |
| Uninstall/day | <5% | >15% |

**If any metric enters danger zone:**
- Investigate root cause
- Fix in next update
- Announce fix in release notes
- Reply to negative reviews

---

## Bug Fix Protocol

**If crash reported:**

1. Read crash stack trace (Play Console → Crashes)
2. Reproduce on emulator if possible
3. Fix in code
4. Test thoroughly
5. Build new signed APK (increment versionCode)
6. Upload to Play Console as new release
7. Set to internal testing first (verify)
8. Promote to production after 2-3 hours
9. Reply to affected users: "Fixed in v1.2.1, please update!"

**Timeline:** Aim to publish fix within 24 hours of report

---

## Content Update Schedule (After Month 1)

**Recommended cadence:**

- **v1.2:** Current (Aug 2026) — Premium packs
- **v1.3:** Week 6 (Sep 2026) — 15 new icons based on feedback
- **v1.4:** Week 10 (Oct 2026) — Second premium pack, more icons
- **v1.5:** Week 14 (Nov 2026) — Third premium pack
- **v2.0:** Week 20+ (Dec 2026+) — Major feature (e.g., IAP customizer)

**Each update should:**
- Add 10-20 new icons
- Fix reported bugs
- Launch one IAP pack (after first release)
- Include detailed release notes

---

## Response Templates

### 5★ Review Reply

```
Thanks for the love! 🖤 We're constantly adding new icons based on user 
feedback. If you have any requests, let us know!
```

### 4★ Review Reply

```
Thanks for rating! What could we improve? We read all feedback and 
prioritize the most-requested icons in updates.
```

### 2-3★ Review Reply (Constructive Feedback)

```
Thanks for the feedback. Can you tell us specifically which icons are 
missing or which feature would help? Drop an issue on GitHub or reply here.
→ https://github.com/angusm99/VOID_UI_Android/issues
```

### 1★ Review Reply (Complaint)

```
Sorry you had trouble! We want to help. Please describe the issue:
- Which launcher are you using?
- Which Android version?
- What icons aren't working?
Email: angusm99@gmail.com or file an issue on GitHub.
```

---

## Play Store Optimization (Weeks 4+)

### Experiment: Store Listing A/B Test

**Option A:** Current description  
**Option B:** Alternative with more emphasis on premium packs

Google Play lets you test which version gets more installs.

Steps:
1. Play Console → Store presence → Main store listing
2. Click "Run experiment"
3. Create variant (change short description or screenshots)
4. Run for 2 weeks
5. See which version wins
6. Apply winning version

---

## Important Links

- **Play Console Analytics:** https://play.google.com/console → Dashboard
- **Review Management:** https://play.google.com/console → Reviews
- **Crash Reporting:** https://play.google.com/console → Crashes & ANRs
- **GitHub Issues (User Feedback):** https://github.com/angusm99/VOID_UI_Android/issues

---

## Checklist: 30-Day Review

After first month, verify:

- [ ] 0% crash rate maintained
- [ ] Rating >= 4.0 stars
- [ ] >100 installs achieved
- [ ] All reviews replied to
- [ ] GitHub issues addressed
- [ ] Feature requests documented
- [ ] Next update planned (v1.3)
- [ ] Premium pack IAP ready to launch

---

**Status:** Ready for post-launch  
**Audience:** You (app maintainer)  
**Last Updated:** 2026-05-22
