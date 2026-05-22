# Roadmap — v1.3 and Beyond

**Current Version:** 1.2 (versionCode 2) — pending Play Store launch  
**Next Major:** v1.3 (versionCode 3) — IAP + new icons

---

## v1.3 — Premium Pack Activation (Target: 4-6 weeks post-launch)

### Goal
Convert the conceptual freemium model into actual revenue. Enable users to purchase premium themed icon packs.

### Features

#### 1. In-App Purchase Implementation
- [ ] Add Google Play Billing Library (v6.1.0)
- [ ] Implement BillingManager class
- [ ] Create PackSelectionActivity UI
- [ ] Handle purchase, acknowledge, restore flows
- [ ] Test in Internal Testing track

#### 2. Pack Selection UI
- [ ] Design Figma mockup
- [ ] Build pack picker interface
- [ ] Show pack previews (4-6 icons per pack)
- [ ] Display pricing per pack
- [ ] "Restore Purchases" button
- [ ] Loading states

#### 3. Dynamic Icon Filtering
- [ ] Read purchased packs from SharedPreferences
- [ ] Filter appfilter.xml output by purchased packs
- [ ] Update icon mappings dynamically

#### 4. New App Icons (15-20)
Based on user feedback, add icons for:
- [ ] Discord (multiple variants)
- [ ] Slack (work/personal variants)
- [ ] LastPass / 1Password
- [ ] Pocket / Read-it-later apps
- [ ] Reddit clients (Apollo, BaconReader, Boost)
- [ ] Mastodon variants
- [ ] WordPress / Substack
- [ ] Stripe / Square / Adyen variants
- [ ] Chrome extensions store
- [ ] User-requested apps

#### 5. Quality Improvements
- [ ] Add launcher detection (which launcher is user using?)
- [ ] Show launcher-specific tips ("Apply VOID UI in Nova → Themes")
- [ ] Better error messages

### Timeline
- **Week 1:** Set up IAP infrastructure
- **Week 2:** Implement BillingManager + UI
- **Week 3:** Build new icons (designer time)
- **Week 4:** Integration testing
- **Week 5:** Internal testing track + bug fixes
- **Week 6:** Public release

### Success Metrics
- 30% of users see pack selection UI (vs. 5% who'd buy any pack)
- 5% conversion to paid (industry avg 2-5%)
- 50+ pack purchases in first 30 days
- Maintain 0% crash rate
- Maintain 4.0+ rating

---

## v1.4 — Visual Refinements (Target: 8-10 weeks post-launch)

### Goal
Polish the visual presentation, add second wave of icons, and address user feedback.

### Features

#### 1. New Icons (15-20 more)
Based on month 1-2 feedback. Likely candidates:
- More AI/ML platforms (open-source models)
- More productivity tools
- Niche apps requested via GitHub issues
- Trending/new apps

#### 2. Settings Activity
- [ ] In-app settings screen
- [ ] Theme preview options
- [ ] Pack ordering/priority
- [ ] About / Credits
- [ ] Privacy policy link
- [ ] Contact developer

#### 3. Color Accent System (Internal)
Lay groundwork for future colour variants:
- [ ] Implement runtime color substitution
- [ ] Test on Sports Zones pack first
- [ ] Document API for future packs

#### 4. Performance
- [ ] Optimize VectorDrawable loading
- [ ] Reduce APK/AAB size if possible
- [ ] Profile on lower-end devices

### Timeline
- **Week 1-2:** UI refinements + new icons
- **Week 3:** Settings screen development
- **Week 4:** Testing & polish
- **Week 5:** Public release

---

## v2.0 — Major Feature (Target: 4-6 months)

### Goal
Add a major user-facing feature that differentiates VOID UI from competitors.

### Possible Features (pick one)

#### Option A: Custom Icon Builder
- In-app icon designer for users
- Choose stroke width, accent color, geometry
- Save custom icons to library
- Apply to specific apps

#### Option B: Live Wallpaper Pack
- Companion live wallpaper matching icon aesthetic
- Available as separate IAP
- Animated minimalist patterns
- Optional widget showing time/date

#### Option C: Adaptive Launcher
- Suggest icon changes based on usage patterns
- "You haven't used Spotify in 3 months. Replace icon?"
- Daily icon rotation feature

#### Option D: Icon Pack Marketplace
- Allow community to submit icon designs
- Approved designs added to pack
- Designers get credit + (optional) revenue share

### Decision Point
After v1.3 launch, gather data on:
- Which packs sell most → expand that aesthetic
- Top user requests → build feature solving them
- Time/skill available → pick feasible option

---

## v3.0 — Platform Expansion (Target: 12-18 months)

### Goal
Expand beyond Android icon pack to broader VOID UI ecosystem.

### Possible Directions

#### Direction A: iOS Companion
- Sister icon pack for iOS
- Same design system
- Cross-platform consistency

#### Direction B: Wallpaper Suite
- Match wallpapers for each pack
- 4K resolution available
- Optional widget integration

#### Direction C: Browser Themes
- Chrome/Firefox extension with matching aesthetic
- Apply VOID UI to web

#### Direction D: SaaS Theme Builder
- Subscription-based theme builder tool
- Drag-and-drop icon designer
- Export to Android, iOS, web
- Higher revenue per customer

---

## Continuous Tasks (Ongoing)

### Monthly
- [ ] Add 10-15 new icons (based on requests)
- [ ] Reply to all reviews
- [ ] Update appfilter.xml with new app packages
- [ ] Test on latest Android versions
- [ ] Monitor crash reports

### Quarterly
- [ ] User survey: what's missing? what's working?
- [ ] Competitor analysis (what are other icon packs doing?)
- [ ] Pricing review (raise/lower prices based on data)
- [ ] Major release planning

### Yearly
- [ ] Full design system review
- [ ] Architecture audit (with Opus or external)
- [ ] Compliance review (GDPR, CCPA, COPPA)
- [ ] Keystore backup verification

---

## Revenue Roadmap

### Year 1 Goals
- **Month 1-3:** Free launch, gather feedback, build community
- **Month 4-6:** Launch IAP (v1.3), validate pricing
- **Month 7-9:** Add color variants, expand premium offerings
- **Month 10-12:** Reach $1,000+ in IAP revenue

### Year 2 Goals
- **Month 13-18:** $5,000+ in revenue
- **Month 19-24:** $10,000+ if growth continues
- Possible: Hire designer for new icons monthly

### Year 3+ Goals
- Platform expansion (iOS, browser themes)
- $25,000+ annual revenue
- Sustainable side income or full-time potential

---

## Decision Framework

When choosing what to build next, evaluate:

| Factor | Weight |
|--------|--------|
| Direct revenue impact | High |
| User retention improvement | High |
| Time to implement | Medium |
| Maintenance burden | Medium |
| Competitive advantage | Medium |
| Personal interest | Low |

**Examples:**
- "Add 15 new icons" → 8 hrs work, low revenue impact (but reduces churn) → Worth doing
- "Custom icon builder" → 80 hrs work, medium revenue (premium feature) → Worth doing
- "iOS version" → 200+ hrs work, unknown revenue → Wait for v3.0

---

## Anti-Features (What NOT to Build)

❌ **Subscription model** — One-time IAP is more user-friendly  
❌ **Ads** — Defeats the privacy-first positioning  
❌ **Analytics** — Same reason  
❌ **In-app browser** — Out of scope for icon pack  
❌ **Cloud sync** — Premium packs don't need it  
❌ **Multiple language support** — Only English needed (icons are visual)  
❌ **Social features** — Sharing icons not core to use case  
❌ **AI-generated icons** — Maintain hand-crafted quality

---

## Inspiration Sources

For new features, check:

- **Other icon packs:** Lawnchair, KWGT, Nucleo Icons
- **Design systems:** Apple SF Symbols, Google Material Symbols
- **Communities:** r/androidthemes, r/userexperience
- **Tools:** Figma, Adobe XD, Sketch
- **Launchers:** Nova settings, Niagara settings (for UX patterns)

---

## Sunset Plan

If the project doesn't gain traction:

### Year 1
- Continue free updates with new icons
- Keep on Play Store indefinitely (low maintenance)
- Use as portfolio piece for design work

### Year 2 (if revenue stagnant)
- Reduce update frequency
- Make all packs free
- Open-source the icon library (CC-BY license)

### Year 3+ (if no engagement)
- Remove from Play Store gracefully
- Migrate Open Source pack to GitHub
- Allow community to fork

---

## Tracking Progress

Use this roadmap as a "north star" but don't be rigid:

- **Reviewed quarterly** — adjust based on data
- **User feedback drives priorities** — listen to actual users
- **Revenue data drives investment** — fund what works
- **Personal interest matters too** — won't ship things you hate

---

**Status:** Living document, updated as project evolves  
**Last Updated:** 2026-05-22  
**Next Review:** After v1.2 launch (4 weeks from launch)
