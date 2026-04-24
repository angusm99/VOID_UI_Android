# VOID UI Icon Pack — ProGuard rules
# No sensitive logic to obfuscate; keeping default safe rules.
-keepattributes *Annotation*
-keepclassmembers class * {
    @android.webkit.JavascriptInterface <methods>;
}
