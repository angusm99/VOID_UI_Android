package com.voidui.iconpack;

import android.content.SharedPreferences;
import android.content.res.Resources;
import android.graphics.Color;
import android.graphics.PorterDuff;
import android.graphics.drawable.GradientDrawable;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.Gravity;
import android.view.View;
import android.view.ViewGroup;
import android.widget.EditText;
import android.widget.FrameLayout;
import android.widget.GridLayout;
import android.widget.HorizontalScrollView;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.SeekBar;
import android.widget.TextView;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

public class MainActivity extends AppCompatActivity {
    private static final String ALL = "All";
    private static final int BLACK = Color.BLACK;
    private static final int WHITE = Color.WHITE;
    private static final int MUTED = Color.rgb(150, 150, 150);
    private static final int FAINT = Color.rgb(64, 64, 64);

    private static final int[] PRESET_COLOURS = {
        WHITE,
        Color.parseColor("#00BFFF"),  // neon blue
        Color.parseColor("#39FF14"),  // neon green
        Color.parseColor("#FF9500"),  // amber
        Color.parseColor("#FFE600"),  // yellow
        Color.parseColor("#FF007F"),  // neon pink
    };

    private static final String PREFS = "void_ui_prefs";
    private static final String PREF_TINT = "icon_tint";

    private final List<IconItem> icons = new ArrayList<>();
    private final List<TextView> categoryButtons = new ArrayList<>();
    private LinearLayout categoryRow;
    private LinearLayout tintRow;
    private GridLayout iconGrid;
    private TextView countView;
    private SharedPreferences prefs;
    private String activeCategory = ALL;
    private String query = "";
    private int currentTint = WHITE;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        prefs = getSharedPreferences(PREFS, MODE_PRIVATE);
        currentTint = prefs.getInt(PREF_TINT, WHITE);
        loadIcons();
        setContentView(buildContent());
        renderTintChips();
        renderCategories();
        renderIcons();
    }

    /** Sets the global icon tint, persists it, and refreshes the UI. */
    private void setTint(int color) {
        currentTint = color;
        if (prefs != null) {
            prefs.edit().putInt(PREF_TINT, color).apply();
        }
        renderTintChips();
        renderIcons();
    }

    private void loadIcons() {
        Resources resources = getResources();
        String[] drawables = resources.getStringArray(R.array.icon_pack_drawables);
        String[] names = resources.getStringArray(R.array.icon_pack_names);

        for (int i = 0; i < drawables.length; i++) {
            String drawableName = drawables[i];
            int resourceId = resources.getIdentifier(drawableName, "drawable", getPackageName());
            if (resourceId == 0) {
                continue;
            }
            String label = i < names.length ? names[i] : titleCase(drawableName);
            icons.add(new IconItem(drawableName, label, categoryFor(drawableName, label), resourceId));
        }
    }

    private View buildContent() {
        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);
        root.setBackgroundColor(BLACK);
        root.setPadding(dp(16), dp(18), dp(16), 0);

        TextView title = new TextView(this);
        title.setText("VOID UI");
        title.setTextColor(WHITE);
        title.setTextSize(28);
        title.setGravity(Gravity.CENTER_VERTICAL);
        title.setLetterSpacing(0.12f);
        title.setTypeface(title.getTypeface(), android.graphics.Typeface.BOLD);
        root.addView(title, new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.WRAP_CONTENT
        ));

        countView = new TextView(this);
        countView.setTextColor(MUTED);
        countView.setTextSize(13);
        countView.setPadding(0, dp(4), 0, dp(14));
        root.addView(countView);

        EditText search = new EditText(this);
        search.setSingleLine(true);
        search.setHint("Search icons");
        search.setHintTextColor(Color.rgb(90, 90, 90));
        search.setTextColor(WHITE);
        search.setTextSize(15);
        search.setPadding(dp(14), 0, dp(14), 0);
        search.setBackgroundColor(Color.rgb(14, 14, 14));
        search.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                query = s.toString().trim().toLowerCase(Locale.US);
                renderIcons();
            }

            @Override
            public void afterTextChanged(Editable s) {
            }
        });
        LinearLayout.LayoutParams searchParams = new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                dp(44)
        );
        root.addView(search, searchParams);

        // Colour tint row (global icon colour)
        TextView tintLabel = new TextView(this);
        tintLabel.setText("ICON COLOUR");
        tintLabel.setTextColor(MUTED);
        tintLabel.setTextSize(11);
        tintLabel.setLetterSpacing(0.10f);
        tintLabel.setPadding(0, dp(14), 0, 0);
        root.addView(tintLabel);

        HorizontalScrollView tintScroll = new HorizontalScrollView(this);
        tintScroll.setHorizontalScrollBarEnabled(false);
        tintScroll.setPadding(0, dp(8), 0, dp(4));
        tintRow = new LinearLayout(this);
        tintRow.setOrientation(LinearLayout.HORIZONTAL);
        tintRow.setGravity(Gravity.CENTER_VERTICAL);
        tintScroll.addView(tintRow);
        root.addView(tintScroll, new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                dp(64)
        ));

        HorizontalScrollView categoryScroll = new HorizontalScrollView(this);
        categoryScroll.setHorizontalScrollBarEnabled(false);
        categoryScroll.setPadding(0, dp(4), 0, dp(10));
        categoryRow = new LinearLayout(this);
        categoryRow.setOrientation(LinearLayout.HORIZONTAL);
        categoryScroll.addView(categoryRow);
        root.addView(categoryScroll, new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                dp(58)
        ));

        ScrollView scrollView = new ScrollView(this);
        scrollView.setFillViewport(false);
        iconGrid = new GridLayout(this);
        iconGrid.setColumnCount(4);
        iconGrid.setPadding(0, dp(8), 0, dp(32));
        scrollView.addView(iconGrid);
        root.addView(scrollView, new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                0,
                1f
        ));

        return root;
    }

    private void renderTintChips() {
        tintRow.removeAllViews();

        for (int color : PRESET_COLOURS) {
            final int c = color;
            boolean isActive = currentTint == color;

            LinearLayout frame = new LinearLayout(this);
            frame.setGravity(Gravity.CENTER);

            GradientDrawable outerBg = new GradientDrawable();
            outerBg.setShape(GradientDrawable.OVAL);
            outerBg.setColor(isActive ? WHITE : Color.TRANSPARENT);
            frame.setBackground(outerBg);

            GradientDrawable innerBg = new GradientDrawable();
            innerBg.setShape(GradientDrawable.OVAL);
            innerBg.setColor(color);
            if (color == WHITE) {
                // faint border so the white chip is visible on black background
                innerBg.setStroke(dp(1), Color.rgb(80, 80, 80));
            }

            View inner = new View(this);
            inner.setBackground(innerBg);
            int innerSize = isActive ? dp(26) : dp(34);
            frame.addView(inner, new LinearLayout.LayoutParams(innerSize, innerSize));

            frame.setOnClickListener(v -> setTint(c));

            LinearLayout.LayoutParams fp = new LinearLayout.LayoutParams(dp(42), dp(42));
            fp.setMargins(0, 0, dp(10), 0);
            tintRow.addView(frame, fp);
        }

        // Custom colour picker chip
        boolean customActive = !isPresetColour(currentTint);

        LinearLayout customFrame = new LinearLayout(this);
        customFrame.setGravity(Gravity.CENTER);

        GradientDrawable customOuter = new GradientDrawable();
        customOuter.setShape(GradientDrawable.OVAL);
        customOuter.setColor(customActive ? WHITE : Color.TRANSPARENT);
        customFrame.setBackground(customOuter);

        FrameLayout customInner = new FrameLayout(this);
        GradientDrawable customInnerBg = new GradientDrawable();
        customInnerBg.setShape(GradientDrawable.OVAL);
        customInnerBg.setColor(customActive ? currentTint : Color.rgb(38, 38, 38));
        if (!customActive) {
            customInnerBg.setStroke(dp(1), Color.rgb(80, 80, 80));
        }
        customInner.setBackground(customInnerBg);

        TextView plusLabel = new TextView(this);
        plusLabel.setText("+");
        plusLabel.setTextColor(customActive ? contrastColour(currentTint) : MUTED);
        plusLabel.setTextSize(18);
        plusLabel.setGravity(Gravity.CENTER);
        plusLabel.setTypeface(plusLabel.getTypeface(), android.graphics.Typeface.BOLD);
        customInner.addView(plusLabel, new FrameLayout.LayoutParams(
                FrameLayout.LayoutParams.MATCH_PARENT,
                FrameLayout.LayoutParams.MATCH_PARENT
        ));

        int customInnerSize = customActive ? dp(26) : dp(34);
        customFrame.addView(customInner, new LinearLayout.LayoutParams(customInnerSize, customInnerSize));

        customFrame.setOnClickListener(v -> showColourPicker());
        tintRow.addView(customFrame, new LinearLayout.LayoutParams(dp(42), dp(42)));
    }

    private boolean isPresetColour(int color) {
        for (int preset : PRESET_COLOURS) {
            if (preset == color) return true;
        }
        return false;
    }

    private int contrastColour(int bg) {
        double lum = 0.299 * Color.red(bg) + 0.587 * Color.green(bg) + 0.114 * Color.blue(bg);
        return lum > 128 ? Color.BLACK : Color.WHITE;
    }

    private void showColourPicker() {
        int startColour = isPresetColour(currentTint) ? WHITE : currentTint;

        LinearLayout layout = new LinearLayout(this);
        layout.setOrientation(LinearLayout.VERTICAL);
        layout.setPadding(dp(24), dp(20), dp(24), dp(8));

        GradientDrawable swatchBg = new GradientDrawable();
        swatchBg.setShape(GradientDrawable.RECTANGLE);
        swatchBg.setCornerRadius(dp(8));
        swatchBg.setColor(startColour);

        View swatch = new View(this);
        swatch.setBackground(swatchBg);
        layout.addView(swatch, new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, dp(52)
        ));

        int[] rgb = {Color.red(startColour), Color.green(startColour), Color.blue(startColour)};
        String[] channels = {"R", "G", "B"};

        for (int i = 0; i < 3; i++) {
            final int idx = i;

            View spacer = new View(this);
            layout.addView(spacer, new LinearLayout.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT, dp(12)
            ));

            TextView lbl = new TextView(this);
            lbl.setText(channels[i]);
            lbl.setTextColor(MUTED);
            lbl.setTextSize(12);
            lbl.setLetterSpacing(0.08f);
            layout.addView(lbl);

            SeekBar bar = new SeekBar(this);
            bar.setMax(255);
            bar.setProgress(rgb[i]);
            bar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
                @Override
                public void onProgressChanged(SeekBar sb, int progress, boolean fromUser) {
                    rgb[idx] = progress;
                    swatchBg.setColor(Color.rgb(rgb[0], rgb[1], rgb[2]));
                }
                @Override public void onStartTrackingTouch(SeekBar sb) {}
                @Override public void onStopTrackingTouch(SeekBar sb) {}
            });
            layout.addView(bar, new LinearLayout.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    ViewGroup.LayoutParams.WRAP_CONTENT
            ));
        }

        new AlertDialog.Builder(this)
                .setTitle("Custom colour")
                .setView(layout)
                .setPositiveButton("Apply", (d, w) -> setTint(Color.rgb(rgb[0], rgb[1], rgb[2])))
                .setNegativeButton("Cancel", null)
                .show();
    }

    private void renderCategories() {
        Map<String, Integer> categoryCounts = new LinkedHashMap<>();
        categoryCounts.put(ALL, icons.size());
        for (IconItem icon : icons) {
            categoryCounts.put(icon.category, categoryCounts.getOrDefault(icon.category, 0) + 1);
        }

        categoryButtons.clear();
        categoryRow.removeAllViews();

        for (Map.Entry<String, Integer> entry : categoryCounts.entrySet()) {
            TextView button = new TextView(this);
            button.setText(entry.getKey() + "  " + entry.getValue());
            button.setTextSize(13);
            button.setGravity(Gravity.CENTER);
            button.setPadding(dp(14), 0, dp(14), 0);
            button.setMinHeight(dp(34));
            button.setTextColor(entry.getKey().equals(activeCategory) ? BLACK : WHITE);
            button.setBackgroundColor(entry.getKey().equals(activeCategory) ? WHITE : Color.rgb(20, 20, 20));
            button.setOnClickListener(v -> {
                activeCategory = entry.getKey();
                renderCategories();
                renderIcons();
            });
            LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(
                    ViewGroup.LayoutParams.WRAP_CONTENT,
                    dp(34)
            );
            params.setMargins(0, 0, dp(8), 0);
            categoryRow.addView(button, params);
            categoryButtons.add(button);
        }
    }

    private void renderIcons() {
        iconGrid.removeAllViews();
        int shown = 0;
        for (IconItem icon : icons) {
            if (!ALL.equals(activeCategory) && !icon.category.equals(activeCategory)) {
                continue;
            }
            if (!query.isEmpty()
                    && !icon.label.toLowerCase(Locale.US).contains(query)
                    && !icon.drawableName.toLowerCase(Locale.US).contains(query)) {
                continue;
            }
            iconGrid.addView(iconTile(icon));
            shown++;
        }
        countView.setText(shown + " of " + icons.size() + " icons");
    }

    private View iconTile(IconItem icon) {
        LinearLayout tile = new LinearLayout(this);
        tile.setOrientation(LinearLayout.VERTICAL);
        tile.setGravity(Gravity.CENTER);
        tile.setPadding(dp(4), dp(8), dp(4), dp(8));

        ImageView image = new ImageView(this);
        image.setImageResource(icon.resourceId);
        image.setAdjustViewBounds(true);
        image.setScaleType(ImageView.ScaleType.FIT_CENTER);
        image.setColorFilter(currentTint, PorterDuff.Mode.SRC_IN);
        tile.addView(image, new LinearLayout.LayoutParams(dp(54), dp(54)));

        TextView label = new TextView(this);
        label.setText(icon.label);
        label.setTextColor(WHITE);
        label.setTextSize(10);
        label.setGravity(Gravity.CENTER);
        label.setMaxLines(2);
        label.setPadding(0, dp(6), 0, 0);
        tile.addView(label, new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT,
                ViewGroup.LayoutParams.WRAP_CONTENT
        ));

        GridLayout.LayoutParams params = new GridLayout.LayoutParams();
        params.width = getResources().getDisplayMetrics().widthPixels / 4 - dp(8);
        params.height = dp(106);
        params.setMargins(0, 0, 0, dp(8));
        tile.setLayoutParams(params);
        tile.setBackgroundColor(FAINT);
        tile.setContentDescription(icon.label + ", " + icon.category);
        return tile;
    }

    private String categoryFor(String drawableName, String label) {
        String id = drawableName.toLowerCase(Locale.US);
        String text = (drawableName + " " + label).toLowerCase(Locale.US);

        if (id.startsWith("circuitry_")) return "Circuitry";
        if (id.startsWith("terminal_")) return "Terminal";
        if (id.startsWith("xeno_")) return "Xenocomm";
        if (id.startsWith("sports_")) return "Sports";
        if (id.startsWith("nation_")) return "Cricket";
        if (id.matches(".*_v[0-9]+$")) return "Variants";

        if (containsAny(text, "ai", "chatgpt", "claude", "gemini", "grok", "copilot", "perplexity", "mistral", "midjourney", "suno", "bot", "neural", "model")) {
            return "AI";
        }
        if (containsAny(text, "instagram", "tiktok", "snapchat", "reddit", "threads", "facebook", "linkedin", "discord", "telegram", "whatsapp", "message", "mail", "gmail", "outlook", "social")) {
            return "Social";
        }
        if (containsAny(text, "spotify", "youtube", "netflix", "music", "podcast", "photo", "gallery", "camera", "media", "video", "sound")) {
            return "Media";
        }
        if (containsAny(text, "bank", "paypal", "wallet", "stripe", "coinbase", "revolut", "robinhood", "amazon", "shop", "receipt", "finance")) {
            return "Finance";
        }
        if (containsAny(text, "github", "gitlab", "docker", "npm", "vscode", "code", "api", "server", "database", "cloud", "terminal", "bluetooth", "nfc", "wifi", "tech")) {
            return "Tech";
        }
        if (containsAny(text, "drive", "file", "folder", "archive", "download", "document", "notes", "storage")) {
            return "Files";
        }
        if (containsAny(text, "map", "travel", "uber", "airbnb", "flight", "waze", "train", "route", "navigation")) {
            return "Travel";
        }
        if (containsAny(text, "health", "fitness", "heart", "sleep", "meditate", "medicine", "pill", "stethoscope")) {
            return "Health";
        }
        if (containsAny(text, "lock", "shield", "privacy", "vpn", "security", "user", "profile", "auth")) {
            return "Security";
        }
        return "Core";
    }

    private boolean containsAny(String text, String... needles) {
        for (String needle : needles) {
            if (text.contains(needle)) {
                return true;
            }
        }
        return false;
    }

    private String titleCase(String value) {
        String[] parts = value.replace('_', ' ').split(" ");
        StringBuilder result = new StringBuilder();
        for (String part : parts) {
            if (part.isEmpty()) {
                continue;
            }
            if (result.length() > 0) {
                result.append(' ');
            }
            result.append(part.substring(0, 1).toUpperCase(Locale.US));
            if (part.length() > 1) {
                result.append(part.substring(1));
            }
        }
        return result.toString();
    }

    private int dp(int value) {
        return Math.round(value * getResources().getDisplayMetrics().density);
    }

    private static final class IconItem {
        final String drawableName;
        final String label;
        final String category;
        final int resourceId;

        IconItem(String drawableName, String label, String category, int resourceId) {
            this.drawableName = drawableName;
            this.label = label;
            this.category = category;
            this.resourceId = resourceId;
        }
    }
}
