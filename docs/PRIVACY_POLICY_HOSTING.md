# Privacy Policy Hosting Guide

**Play Store Requirement:** Every app must have a public URL to its privacy policy.

**VOID UI privacy policy location:** `docs/privacy-policy.md` in GitHub repo

---

## Option 1: GitHub Pages (Recommended — Free, Automatic)

### Step 1: Enable GitHub Pages

1. Go to your GitHub repo: https://github.com/angusm99/VOID_UI_Android
2. Click **Settings** (top right)
3. Scroll down to **Pages** section
4. Under "Source," select:
   - Branch: `master`
   - Folder: `/docs`
   - Click **Save**
5. Wait 1-2 minutes for deployment

### Step 2: Access Your Privacy Policy

GitHub automatically generates a public URL:

```
https://angusm99.github.io/VOID_UI_Android/privacy-policy.md
```

Or if `.md` doesn't render nicely, convert to HTML first (see Step 3).

### Step 3: Convert Markdown to HTML (Optional, Better Formatting)

Your `privacy-policy.md` can be viewed as HTML:

```
https://angusm99.github.io/VOID_UI_Android/privacy-policy.html
```

**To auto-convert:**

1. In your repo, create `docs/_config.yml`:
```yaml
markdown: kramdown
theme: jekyll-theme-minimal
```

2. Commit and push
3. GitHub automatically renders `.md` files with styling

### Step 4: Verify It's Public

1. Open the privacy policy URL in incognito browser (not logged in)
2. Should load without errors
3. Copy the full URL

### Step 5: Add to Play Console

In Google Play Console:
- **App Privacy** → paste your GitHub Pages URL
- Example: `https://angusm99.github.io/VOID_UI_Android/privacy-policy`

---

## Option 2: Alternative Hosts (If GitHub Pages doesn't work)

### Google Sites (Free)

1. Go to https://sites.google.com
2. Create new site: "VOID UI Privacy Policy"
3. Copy privacy policy text from `docs/privacy-policy.md`
4. Publish
5. Get public URL, add to Play Console

### Vercel (Free)

1. Deploy your docs folder to Vercel
2. Get public URL
3. Add to Play Console

---

## Privacy Policy URL Format

**For Play Console, use:**

```
https://angusm99.github.io/VOID_UI_Android/privacy-policy.md
```

Or (if converted to HTML):

```
https://angusm99.github.io/VOID_UI_Android/privacy-policy.html
```

---

## Current Privacy Policy Content

Your `docs/privacy-policy.md` already contains:

✅ Last updated date  
✅ Data collection statement (zero collection)  
✅ No account/analytics/advertising  
✅ Third-party services disclaimer  
✅ Children's privacy compliance  
✅ Change notification policy  
✅ Contact information  
✅ GitHub issues link for support  

**No changes needed** — it's Play Store compliant.

---

## Verification Checklist

- [ ] GitHub Pages enabled in repo settings (source: `/docs`, branch: `master`)
- [ ] Wait 2-3 minutes for deployment
- [ ] Privacy policy URL works in incognito browser
- [ ] Content is readable and public (no login required)
- [ ] URL copied and saved
- [ ] Ready to paste into Play Console

---

## Helpful Links

- GitHub Pages documentation: https://pages.github.com/
- Google Play Console privacy policy requirements: https://support.google.com/googleplay/android-developer/answer/10787469
- Markdown rendering: https://guides.github.com/features/mastering-markdown/

---

**Status:** Ready to deploy  
**Recommended Host:** GitHub Pages (automatic, free, included with repo)
