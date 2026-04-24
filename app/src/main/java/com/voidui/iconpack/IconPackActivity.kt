package com.voidui.iconpack

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

/**
 * VOID UI Icon Pack — Icon Pack Activity
 *
 * This activity is the entry point for launcher apps (Nova, Niagara, Apex, Action, etc.)
 * when they look for icon packs. The actual icon mapping is defined in res/xml/appfilter.xml.
 * No UI is needed here — launchers query the package directly for drawables.
 */
class IconPackActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Launchers don't need a UI from this activity — finish immediately
        // and let them read appfilter.xml via PackageManager
        finish()
    }
}
