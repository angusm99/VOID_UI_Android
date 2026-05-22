# In-App Purchase (IAP) Implementation Guide

**Goal:** Enable users to purchase premium icon packs  
**Phase:** After v1.2 launch, planned for v1.3 update  
**Estimated Effort:** 3-5 days

---

## Premium Pack IAP Strategy

### Pricing Tiers (Recommended)

| Pack | Price | Notes |
|------|-------|-------|
| **CIRCUITRY** (94 icons) | $1.99 USD | Best seller — tech aesthetic |
| **TERMINAL** (108 icons) | $1.99 USD | Retro fans, hacker aesthetic |
| **XENOCOMM** (123 icons) | $2.99 USD | Most icons, sci-fi premium |
| **CRICKET NATIONS** (16 icons) | $0.99 USD | Niche, regional appeal |
| **SPORTS ZONES** (30 icons) | $1.49 USD | Sports app users |
| **All-In-One Bundle** | $5.99 USD | All 5 packs (save 30%) |

**Regional pricing** is automatically converted by Play Store.

---

## Implementation Steps

### Step 1: Enable Billing in Play Console

1. **Play Console → Monetize → Products**
2. Click **Create new product** (one for each pack)
3. Fill in:
   - **Product ID:** `voidui_pack_circuitry` (lowercase, no spaces)
   - **Name:** "CIRCUITRY Premium Pack"
   - **Description:** "94 neon circuit board icons + 5 accent colour variants"
   - **Price:** $1.99 USD
4. **Save** as **Active**

**Repeat for all 5 packs + bundle.**

---

### Step 2: Add Google Play Billing Library

In `app/build.gradle`:

```gradle
dependencies {
    implementation 'androidx.appcompat:appcompat:1.6.1'
    implementation 'com.google.android.material:material:1.11.0'
    
    // Add this:
    implementation 'com.android.billingclient:billing-ktx:6.1.0'
}
```

Sync Gradle.

---

### Step 3: Create BillingClient

**File:** `app/src/main/java/com/voidui/iconpack/BillingManager.java`

```java
package com.voidui.iconpack;

import android.content.Context;
import android.util.Log;
import androidx.annotation.NonNull;
import com.android.billingclient.api.*;
import java.util.Arrays;
import java.util.List;

public class BillingManager {
    private static final String TAG = "BillingManager";
    
    public static final String SKU_CIRCUITRY = "voidui_pack_circuitry";
    public static final String SKU_TERMINAL = "voidui_pack_terminal";
    public static final String SKU_XENOCOMM = "voidui_pack_xenocomm";
    public static final String SKU_NATIONS = "voidui_pack_nations";
    public static final String SKU_SPORTS = "voidui_pack_sports";
    public static final String SKU_BUNDLE = "voidui_pack_bundle";
    
    private static final List<String> ALL_SKUS = Arrays.asList(
        SKU_CIRCUITRY, SKU_TERMINAL, SKU_XENOCOMM, 
        SKU_NATIONS, SKU_SPORTS, SKU_BUNDLE
    );
    
    private BillingClient billingClient;
    private Context context;
    
    public BillingManager(Context context) {
        this.context = context;
        initializeBillingClient();
    }
    
    private void initializeBillingClient() {
        billingClient = BillingClient.newBuilder(context)
            .enablePendingPurchases()
            .setListener((billingResult, purchases) -> {
                if (billingResult.getResponseCode() == BillingClient.BillingResponseCode.OK 
                    && purchases != null) {
                    for (Purchase purchase : purchases) {
                        handlePurchase(purchase);
                    }
                }
            })
            .build();
        
        billingClient.startConnection(new BillingClientStateListener() {
            @Override
            public void onBillingSetupFinished(@NonNull BillingResult billingResult) {
                if (billingResult.getResponseCode() == BillingClient.BillingResponseCode.OK) {
                    queryAvailableProducts();
                }
            }
            
            @Override
            public void onBillingServiceDisconnected() {
                Log.w(TAG, "Billing service disconnected");
            }
        });
    }
    
    private void queryAvailableProducts() {
        List<QueryProductDetailsParams.Product> productList = new java.util.ArrayList<>();
        for (String sku : ALL_SKUS) {
            productList.add(QueryProductDetailsParams.Product.newBuilder()
                .setProductId(sku)
                .setProductType(BillingClient.ProductType.INAPP)
                .build());
        }
        
        QueryProductDetailsParams params = QueryProductDetailsParams.newBuilder()
            .setProductList(productList)
            .build();
        
        billingClient.queryProductDetailsAsync(params, (billingResult, productDetails) -> {
            if (billingResult.getResponseCode() == BillingClient.BillingResponseCode.OK) {
                // Products loaded, ready to display
                Log.d(TAG, "Products loaded: " + productDetails.size());
            }
        });
    }
    
    private void handlePurchase(Purchase purchase) {
        if (purchase.getPurchaseState() == Purchase.PurchaseState.PURCHASED) {
            // Save to SharedPreferences that pack is unlocked
            PreferenceManager.setPackPurchased(context, purchase.getSkus().get(0), true);
            
            // Acknowledge purchase (one-time, required by Google)
            if (!purchase.isAcknowledged()) {
                AcknowledgePurchaseParams params = AcknowledgePurchaseParams.newBuilder()
                    .setPurchaseToken(purchase.getPurchaseToken())
                    .build();
                
                billingClient.acknowledgePurchase(params, billingResult -> {
                    if (billingResult.getResponseCode() == BillingClient.BillingResponseCode.OK) {
                        Log.d(TAG, "Purchase acknowledged");
                    }
                });
            }
        }
    }
    
    public void purchase(android.app.Activity activity, String sku) {
        // Query, then launch billing flow
        // Implementation depends on product details cached
    }
    
    public boolean isPackUnlocked(String sku) {
        return PreferenceManager.isPackPurchased(context, sku);
    }
    
    public void onDestroy() {
        if (billingClient != null) {
            billingClient.endConnection();
        }
    }
}
```

---

### Step 4: SharedPreferences Manager

**File:** `app/src/main/java/com/voidui/iconpack/PreferenceManager.java`

```java
package com.voidui.iconpack;

import android.content.Context;
import android.content.SharedPreferences;

public class PreferenceManager {
    private static final String PREFS_NAME = "voidui_prefs";
    
    public static void setPackPurchased(Context context, String sku, boolean purchased) {
        SharedPreferences prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE);
        prefs.edit().putBoolean(sku, purchased).apply();
    }
    
    public static boolean isPackPurchased(Context context, String sku) {
        SharedPreferences prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE);
        return prefs.getBoolean(sku, false);
    }
    
    public static void clearAllPurchases(Context context) {
        // For testing/refunds
        SharedPreferences prefs = context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE);
        prefs.edit().clear().apply();
    }
}
```

---

### Step 5: Pack Selection UI

**File:** `app/src/main/java/com/voidui/iconpack/PackSelectionActivity.java`

```java
package com.voidui.iconpack;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import androidx.appcompat.app.AppCompatActivity;

public class PackSelectionActivity extends AppCompatActivity {
    
    private BillingManager billingManager;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pack_selection);
        
        billingManager = new BillingManager(this);
        setupPackButtons();
    }
    
    private void setupPackButtons() {
        Button circuitryButton = findViewById(R.id.button_circuitry);
        circuitryButton.setOnClickListener(v -> {
            if (billingManager.isPackUnlocked(BillingManager.SKU_CIRCUITRY)) {
                applyPack("circuitry");
            } else {
                billingManager.purchase(this, BillingManager.SKU_CIRCUITRY);
            }
        });
        
        // Repeat for all 5 packs + bundle
    }
    
    private void applyPack(String packName) {
        // Update icon mappings in appfilter.xml dynamically
        // OR redirect user to launcher settings to apply pack
        // ... implementation details
    }
}
```

---

### Step 6: Dynamic Icon Filtering

Premium packs hide icons until purchase. Two approaches:

**Approach A: Multiple appfilter.xml files (Simpler)**
- `appfilter_free.xml` — Core 288 icons
- `appfilter_circuitry.xml` — Adds 94 circuitry mappings
- `appfilter_terminal.xml` — Adds 108 terminal mappings
- Etc.

**Approach B: Single appfilter.xml + Runtime Filtering (Recommended)**
- All mappings in one file
- App reads SharedPreferences on launch
- Returns filtered list to launcher

**Implementation:**
```java
// In IconPackContentProvider or similar
public class IconPackProvider {
    public static String getAppfilterContent(Context context) {
        StringBuilder filtered = new StringBuilder();
        // Read appfilter.xml
        // Skip lines that reference premium packs unless purchased
        // Return filtered content
        return filtered.toString();
    }
}
```

---

### Step 7: Testing IAP

**Test Configuration:**

1. **Internal Testing Track**
   - Sign signed AAB with same keystore
   - Upload to Internal Testing
   - Add yourself as tester (license email in Play Console)
   - Install via Play Store with test account
   - Verify IAP flow

2. **Test Cards (Google Play)**
   - Add test cards in Play Console → Settings → License testing
   - Or use Google's test card numbers
   - Verify purchase, restore, refund flows

3. **Test Refund/Cancellation**
   - In Play Console → Orders, cancel test purchase
   - Verify SharedPreferences updates
   - Verify locked icons return to locked state

---

### Step 8: Add Restore Purchases UI

```java
public void onRestorePurchases(View v) {
    QueryPurchasesParams params = QueryPurchasesParams.newBuilder()
        .setProductType(BillingClient.ProductType.INAPP)
        .build();
    
    billingClient.queryPurchasesAsync(params, (billingResult, purchases) -> {
        if (billingResult.getResponseCode() == BillingClient.BillingResponseCode.OK) {
            for (Purchase purchase : purchases) {
                if (purchase.getPurchaseState() == Purchase.PurchaseState.PURCHASED) {
                    PreferenceManager.setPackPurchased(context, 
                        purchase.getSkus().get(0), true);
                }
            }
            // Refresh UI
        }
    });
}
```

---

## Pricing Strategy

### Tier 1: Conservative ($1.49-$1.99 per pack)
- Low risk for users to buy
- Higher conversion rate
- Total possible: $5.96 for all 5 packs

### Tier 2: Premium ($2.99 per pack)
- Higher perceived value
- Lower conversion rate
- Total possible: $14.95 for all 5 packs

### Tier 3: Bundle ($5.99 all-in-one)
- Best value perception
- "Save 30%" prompt
- Increases avg revenue per user (ARPU)

### Tier 4: Free + Premium "Donation" Model
- All packs free
- Optional "support me" donation ($1.99-$9.99)
- More users, less revenue per user

**Recommendation:** Start with Tier 1 + bundle. Adjust after 30 days based on data.

---

## A/B Testing Pricing

After 100+ premium pack purchases:

1. Create 2 product versions:
   - SKU_v1: $1.99
   - SKU_v2: $2.99
2. Show different prices to different user segments
3. Measure conversion rate by region
4. Adjust pricing per region

---

## Revenue Projections

### Conservative Estimate (Year 1):
- **1,000 free installs** (achievable)
- **5% conversion to paid** (industry avg: 2-5%)
- **50 paid customers**
- **Avg purchase: $2.50** (1 pack)
- **Year 1 revenue: $125**

### Realistic Estimate (Year 1):
- **5,000 free installs**
- **7% conversion to paid**
- **350 paid customers**
- **Avg purchase: $4.00** (2 packs)
- **Year 1 revenue: $1,400**

### Optimistic Estimate (Year 1):
- **20,000 free installs**
- **12% conversion to paid**
- **2,400 paid customers**
- **Avg purchase: $6.00** (3+ packs)
- **Year 1 revenue: $14,400**

---

## Marketing IAP Properly

### App Description Update

```
PRIORITY UPDATE: VOID UI now offers 5 premium themed icon packs!

🛒 PREMIUM PACKS AVAILABLE:
• CIRCUITRY ($1.99) — Neon circuit board aesthetic
• TERMINAL ($1.99) — Retro amber CRT phosphor glow
• XENOCOMM ($2.99) — Alien bioluminescent sci-fi
• CRICKET NATIONS ($0.99) — Nation symbols
• SPORTS ZONES ($1.49) — Team colour-adaptive icons

OR purchase all 5 packs in our bundle for $5.99 (save 30%).

Try the free tier first — 288 icons covering popular apps.
Premium packs are completely optional.
```

### Update Description (App Store)

```
v1.3 Update: Premium Packs Available

You can now unlock 5 themed icon packs via In-App Purchase. 
Try the free version first, then choose your favorite aesthetic.

✓ All purchases are one-time (no subscriptions)
✓ All purchases work forever (no expiration)
✓ Restore purchases on any device with same Google account
```

---

## Launch Day Marketing

When v1.3 launches (with IAP):

1. **Day 0 (Launch):**
   - Update Play Store description with IAP info
   - Post on r/androidthemes: "Premium packs now available"
   - Email past users: "New themed packs unlocked"

2. **Day 7:**
   - Highlight specific pack (e.g., "CIRCUITRY is selling out!")
   - Showcase pack on social media
   - Run small Reddit ad ($10-20 budget)

3. **Day 30:**
   - Compare premium vs. free retention
   - Adjust pricing if conversion <2%
   - Plan v1.4 with another pack

---

## Error Handling

Always handle these scenarios:

- **No internet** during purchase → Save intent, retry on reconnect
- **Purchase declined** → Show clear error message, suggest alternative
- **Refund processed** → Update local state, hide premium icons
- **Account switch** → Re-verify purchases, restore correct entitlements

---

## Compliance Notes

- **Google Play takes 15% commission** (down from 30% for first $1M)
- **Refunds:** Users can request refund within 48 hours
- **Subscriptions:** N/A (one-time purchases only)
- **Renewal:** N/A (lifetime access)

---

**Status:** Implementation guide ready  
**Phase:** Post-v1.2 launch  
**Estimated Implementation Time:** 3-5 days
