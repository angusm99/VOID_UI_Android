package com.voidui.iconpack

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

/**
 * VOID UI Icon Pack — Main Activity
 *
 * This screen is shown when the user opens the icon pack app directly.
 * It displays basic info and instructions for applying the pack in a launcher.
 * The actual icon pack functionality is handled via intent-filters in the manifest.
 */
class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
}
