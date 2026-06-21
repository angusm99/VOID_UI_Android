"""
Strip opaque full-canvas background plates from every drawable so the whole
pack tints cleanly (a baked plate gets painted solid by SRC_IN under any tint).

A plate = a fill-only path (no stroke), opaque fill, whose pathData starts at
the origin (M0 ...). Removing it is a no-op at the white default (the gallery
tile + launcher already provide black) but fixes the solid-square-under-tint bug.
Skips a file if stripping would leave it with no paths.
"""
import re
from pathlib import Path

RES = Path(r"C:\Users\User\CLAUDE\VOID_UI\02_ANDROID_ICON_PACK_APP\VOID_UI_Android\app\src\main\res")
DIRS = [RES / "drawable", RES / "drawable-nodpi"]

PLATE_START = re.compile(r"M\s*0[\s,cChHvVlLzZ]")

def strip_plates(text):
    removed = 0
    def repl(m):
        nonlocal removed
        tag = m.group(0)
        if "strokeColor" in tag:
            return tag
        fc = re.search(r'fillColor="([^"]*)"', tag)
        pd = re.search(r'pathData="([^"]*)"', tag)
        if not fc or not pd:
            return tag
        fill = fc.group(1)
        if fill == "@android:color/transparent" or fill.upper() == "#00000000":
            return tag
        if PLATE_START.match(pd.group(1).lstrip()):
            removed += 1
            return ""
        return tag
    new = re.sub(r"<path\b.*?/>", repl, text, flags=re.DOTALL)
    return new, removed

def main():
    files_changed = total_removed = skipped = 0
    for d in DIRS:
        for f in sorted(d.glob("*.xml")):
            text = f.read_text(encoding="utf-8")
            new, removed = strip_plates(text)
            if removed == 0:
                continue
            if "<path" not in new:  # guard: never empty an icon
                skipped += 1
                continue
            f.write_text(new, encoding="utf-8")
            files_changed += 1
            total_removed += removed
    print(f"files changed: {files_changed}")
    print(f"plates removed: {total_removed}")
    print(f"skipped (would empty): {skipped}")

if __name__ == "__main__":
    main()
