"""
Normalise every icon's effective stroke weight to match the Circuitry pack (14px
at the 512 canvas), so the whole pack reads with one consistent line weight.

Per icon: compute the median effective stroke (strokeWidth x group-scale, scaled
to a 512 reference), then multiply every strokeWidth by target/median. This
preserves each icon's internal stroke ratios while centring it on 14px.

Idempotent: re-running finds median ~= target and rescales by ~1.0.
Skips packs already at 14 (circuitry, nation) and the generated mono packs
(xeno, terminal) which the generator already emits at 14.
"""
import re, statistics, xml.etree.ElementTree as ET
from pathlib import Path

RES = Path(r"C:\Users\User\CLAUDE\VOID_UI\02_ANDROID_ICON_PACK_APP\VOID_UI_Android\app\src\main\res")
DIRS = [RES / "drawable", RES / "drawable-nodpi"]
ANS = "{http://schemas.android.com/apk/res/android}"
TARGET = 14.0
SKIP = ("circuitry_", "nation_", "xeno_", "terminal_")

def group_scale(root):
    gs = root.findall(".//group")
    return max([float(g.get(ANS + "scaleX", "1")) for g in gs] + [1.0])

def median_eff(path_xml):
    root = ET.fromstring(path_xml)
    vw = float(root.get(ANS + "viewportWidth", "512"))
    scale = group_scale(root)
    effs = [float(p.get(ANS + "strokeWidth")) * scale / vw * 512
            for p in root.findall(".//path")
            if p.get(ANS + "strokeColor") and p.get(ANS + "strokeWidth")]
    return statistics.median(effs) if effs else None

def main():
    # Use drawable/ as the source of truth for which files & factors; mirror to nodpi.
    changed = skipped = 0
    for f in sorted((RES / "drawable").glob("*.xml")):
        if f.stem.startswith(SKIP):
            continue
        text = f.read_text(encoding="utf-8")
        try:
            med = median_eff(text)
        except ET.ParseError:
            continue
        if med is None:            # no strokes (filled icon) — nothing to scale
            continue
        if abs(med - TARGET) < 0.6:  # already on target
            skipped += 1
            continue
        factor = TARGET / med
        def scale_w(m):
            return f'android:strokeWidth="{round(float(m.group(1)) * factor, 2)}"'
        new = re.sub(r'android:strokeWidth="([\d.]+)"', scale_w, text)
        for d in DIRS:
            tgt = d / f.name
            if tgt.exists():
                tgt.write_text(new, encoding="utf-8")
        changed += 1
    print(f"normalised: {changed}, already-on-target skipped: {skipped}")

if __name__ == "__main__":
    main()
