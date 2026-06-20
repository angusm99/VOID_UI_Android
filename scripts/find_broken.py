"""
Finds broken drawables (empty or black-square-only) and maps them to source SVGs.
Prints a report plus a JSON manifest for the repair script.
"""
import json, os, xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(r"C:\Users\User\CLAUDE\VOID_UI")
MASTER = ROOT / "01_ICON_PACK_MASTER" / "ICON_MASTER"
DRAWABLE = ROOT / "02_ANDROID_ICON_PACK_APP" / "VOID_UI_Android" / "app" / "src" / "main" / "res" / "drawable"

ANS = "http://schemas.android.com/apk/res/android"

def is_broken(xml_path):
    """
    VectorDrawable: <path> elements have no namespace on the tag, only on attrs.
    Attributes use {http://schemas.android.com/apk/res/android}attrName.
    """
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        paths = root.findall('.//path')  # no namespace on element tag
        if len(paths) == 0:
            return "empty"
        if len(paths) == 1:
            p = paths[0]
            fill = p.get(f'{{{ANS}}}fillColor', '')
            pd = p.get(f'{{{ANS}}}pathData', '')
            stroke = p.get(f'{{{ANS}}}strokeColor', '')
            # Black background plate only — fill is black, no stroke, short path
            if fill in ('#FF000000', '#000000') and not stroke and 'M0 0' in pd and len(pd) < 30:
                return "black_only"
    except Exception:
        return "parse_error"
    return None

def find_source_svg(stem):
    """Search all ICON_MASTER subdirs for a matching SVG."""
    candidates = []
    for svg in MASTER.rglob(f"{stem}.svg"):
        candidates.append(svg)
    return candidates

broken = []
for xml_file in sorted(DRAWABLE.glob("*.xml")):
    status = is_broken(xml_file)
    if status:
        stem = xml_file.stem
        sources = find_source_svg(stem)
        broken.append({
            "drawable": xml_file.name,
            "stem": stem,
            "status": status,
            "sources": [str(s) for s in sources],
        })

fixable = [b for b in broken if b["sources"]]
unfixable = [b for b in broken if not b["sources"]]

print(f"Total broken: {len(broken)}")
print(f"  Fixable (have source SVG): {len(fixable)}")
print(f"  Unfixable (no source found): {len(unfixable)}")
print()
print("=== FIXABLE ===")
for b in fixable:
    print(f"  [{b['status']:12}] {b['stem']}  ->  {b['sources'][0]}")
print()
print("=== UNFIXABLE (will be removed) ===")
for b in unfixable:
    print(f"  [{b['status']:12}] {b['stem']}")

manifest_path = Path(__file__).parent / "broken_manifest.json"
manifest_path.write_text(json.dumps({"fixable": fixable, "unfixable": unfixable}, indent=2), encoding="utf-8")
print(f"\nManifest written to {manifest_path}")
