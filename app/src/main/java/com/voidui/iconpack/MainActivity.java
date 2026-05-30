package com.voidui.iconpack;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;

import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        TextView iconsCount = findViewById(R.id.icons_count_textview);
        String count = getString(R.string.icon_count);
        iconsCount.setText(getString(R.string.icons_count_format, count));
    }
}
