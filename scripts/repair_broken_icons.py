"""
Repairs 59 broken drawables:
  - 14 fixable: regenerated from source SVGs (by exact or ic_-stripped name)
  - 45 unfixable: removed from drawable/, drawable-nodpi/, icon_pack.xml,
    and all three appfilter.xml copies
"""
import math, re, xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(r"C:\Users\User\CLAUDE\VOID_UI")
MASTER = ROOT / "01_ICON_PACK_MASTER" / "ICON_MASTER"
ANDROID = ROOT / "02_ANDROID_ICON_PACK_APP" / "VOID_UI_Android" / "app" / "src" / "main"
RES = ANDROID / "res"

# ─── SVG → VectorDrawable converter (from regenerate_master_svg_vectors.py) ──

COLOR_MAP = {
    "black": "#FF000000", "white": "#FFFFFFFF",
    "#fff": "#FFFFFFFF", "#ffffff": "#FFFFFFFF",
    "#000": "#FF000000", "#000000": "#FF000000",
    "currentcolor": "#FFFFFFFF",  # CSS inherit → white on AMOLED black
    "currentColor": "#FFFFFFFF",
}

def clean_number(v):
    n = float(v)
    return str(int(round(n))) if abs(n - round(n)) < 1e-6 else f"{n:.3f}".rstrip("0").rstrip(".")

def attr_float(attrs, name, default=0):
    raw = attrs.get(name)
    if raw is None:
        return default
    return float(str(raw).replace("px", ""))

def android_color(value):
    if not value or value == "none":
        return None
    if value in COLOR_MAP:
        return COLOR_MAP[value]
    lo = value.lower()
    if lo in COLOR_MAP:
        return COLOR_MAP[lo]
    if lo == "currentcolor":
        return "#FFFFFFFF"
    if lo.startswith("#"):
        h = lo[1:]
        if len(h) == 3:
            h = "".join(c*2 for c in h)
        if len(h) == 6:
            return "#FF" + h.upper()
        if len(h) == 8:
            return "#" + h.upper()
    return value

def alpha(attrs, kind):
    vals = []
    if "opacity" in attrs:
        vals.append(float(attrs["opacity"]))
    if f"{kind}-opacity" in attrs:
        vals.append(float(attrs[f"{kind}-opacity"]))
    if not vals:
        return None
    r = 1.0
    for v in vals:
        r *= v
    return clean_number(r)

def parse_style(style):
    res = {}
    if not style:
        return res
    for part in style.split(";"):
        if ":" in part:
            k, v = part.split(":", 1)
            res[k.strip()] = v.strip()
    return res

def parse_translate(transform):
    if not transform:
        return 0.0, 0.0
    m = re.search(r"translate\(([^,\s)]+)[,\s]+([^,\s)]+)\)", transform)
    if not m:
        m = re.search(r"translate\(([^,\s)]+)\)", transform)
        if not m:
            return 0.0, 0.0
        return float(m.group(1)), 0.0
    return float(m.group(1)), float(m.group(2))

def local_name(tag):
    return tag.split("}", 1)[-1]

def inherited_attrs(parent, element):
    attrs = dict(parent)
    attrs.update(parse_style(element.attrib.get("style")))
    for k, v in element.attrib.items():
        if k != "style":
            attrs[k] = v
    return attrs

def circle_path(cx, cy, r):
    x1 = clean_number(cx - r)
    x2 = clean_number(cx + r)
    y = clean_number(cy)
    rv = clean_number(r)
    return f"M{x1},{y} A{rv},{rv} 0,1 0 {x2},{y} A{rv},{rv} 0,1 0 {x1},{y}"

def rect_path(x, y, w, h, rx=0):
    x2, y2 = x + w, y + h
    if rx <= 0:
        return f"M{clean_number(x)},{clean_number(y)} H{clean_number(x2)} V{clean_number(y2)} H{clean_number(x)} Z"
    rx = min(rx, w/2, h/2)
    return (
        f"M{clean_number(x+rx)},{clean_number(y)} "
        f"H{clean_number(x2-rx)} Q{clean_number(x2)},{clean_number(y)} {clean_number(x2)},{clean_number(y+rx)} "
        f"V{clean_number(y2-rx)} Q{clean_number(x2)},{clean_number(y2)} {clean_number(x2-rx)},{clean_number(y2)} "
        f"H{clean_number(x+rx)} Q{clean_number(x)},{clean_number(y2)} {clean_number(x)},{clean_number(y2-rx)} "
        f"V{clean_number(y+rx)} Q{clean_number(x)},{clean_number(y)} {clean_number(x+rx)},{clean_number(y)} Z"
    )

def points_path(points, close):
    coords = [float(v) for v in re.findall(r"-?\d+(?:\.\d+)?", points or "")]
    if len(coords) < 4:
        return None
    pairs = list(zip(coords[0::2], coords[1::2]))
    cmds = [f"M{clean_number(pairs[0][0])},{clean_number(pairs[0][1])}"]
    cmds.extend(f"L{clean_number(x)},{clean_number(y)}" for x, y in pairs[1:])
    if close:
        cmds.append("Z")
    return " ".join(cmds)

def path_style(attrs):
    fill = android_color(attrs.get("fill", "none"))
    stroke = android_color(attrs.get("stroke"))
    vals = []
    if fill:
        vals.append(("android:fillColor", fill))
        a = alpha(attrs, "fill")
        if a:
            vals.append(("android:fillAlpha", a))
    if stroke:
        vals.append(("android:strokeColor", stroke))
        vals.append(("android:strokeWidth", clean_number(attr_float(attrs, "stroke-width", 1))))
        if "stroke-linecap" in attrs:
            vals.append(("android:strokeLineCap", attrs["stroke-linecap"]))
        if "stroke-linejoin" in attrs:
            vals.append(("android:strokeLineJoin", attrs["stroke-linejoin"]))
        a = alpha(attrs, "stroke")
        if a:
            vals.append(("android:strokeAlpha", a))
    return vals

def emit_path(path_data, attrs):
    if not path_data:
        return []
    style = path_style(attrs)
    if not style:
        style = [("android:fillColor", "#00000000")]
    lines = ["    <path"]
    for k, v in style:
        lines.append(f'        {k}="{v}"')
    lines.append(f'        android:pathData="{path_data}"/>')
    return lines

def collect_paths(element, inherited, tx=0.0, ty=0.0):
    attrs = inherited_attrs(inherited, element)
    dx, dy = parse_translate(attrs.get("transform"))
    tx += dx
    ty += dy
    tag = local_name(element.tag)
    paths = []
    if tag == "path":
        paths.extend(emit_path(attrs.get("d"), attrs))
    elif tag == "line":
        paths.extend(emit_path(
            f"M{clean_number(attr_float(attrs,'x1')+tx)},{clean_number(attr_float(attrs,'y1')+ty)} "
            f"L{clean_number(attr_float(attrs,'x2')+tx)},{clean_number(attr_float(attrs,'y2')+ty)}",
            attrs))
    elif tag == "circle":
        paths.extend(emit_path(circle_path(attr_float(attrs,"cx")+tx, attr_float(attrs,"cy")+ty, attr_float(attrs,"r")), attrs))
    elif tag == "rect":
        paths.extend(emit_path(rect_path(attr_float(attrs,"x")+tx, attr_float(attrs,"y")+ty,
                                         attr_float(attrs,"width"), attr_float(attrs,"height"),
                                         attr_float(attrs,"rx")), attrs))
    elif tag == "polyline":
        paths.extend(emit_path(points_path(attrs.get("points"), False), attrs))
    elif tag == "polygon":
        paths.extend(emit_path(points_path(attrs.get("points"), True), attrs))
    for child in element:
        paths.extend(collect_paths(child, attrs, tx, ty))
    return paths

def convert_svg(svg_path):
    tree = ET.parse(svg_path)
    root = tree.getroot()
    vb = root.attrib.get("viewBox", "0 0 512 512").split()
    vw = vb[2] if len(vb) == 4 else "512"
    vh = vb[3] if len(vb) == 4 else "512"
    paths = collect_paths(root, {})
    return "\n".join([
        '<vector xmlns:android="http://schemas.android.com/apk/res/android"',
        '    android:width="512dp"',
        '    android:height="512dp"',
        f'    android:viewportWidth="{vw}"',
        f'    android:viewportHeight="{vh}">',
        *paths,
        '</vector>',
        '',
    ])

# ─── Fix map: drawable_stem → source SVG ─────────────────────────────────────

FIXABLE = {
    # exact name match
    "chatgpt":    MASTER / "02_VOID_UI" / "ai_brands" / "chatgpt.svg",
    "code":       MASTER / "04_SYSTEM_UICONS" / "code.svg",
    "grok":       MASTER / "02_VOID_UI" / "ai_brands" / "grok.svg",
    "ic_bluetooth": MASTER / "05_CIRCUITRY" / "ic_bluetooth.svg",
    "record":     MASTER / "04_SYSTEM_UICONS" / "record.svg",
    "target":     MASTER / "04_SYSTEM_UICONS" / "target.svg",
    # ic_-stripped matches
    "ic_download":    MASTER / "04_SYSTEM_UICONS" / "download.svg",
    "ic_key":         MASTER / "02_VOID_UI" / "core" / "key.svg",
    "ic_lightning":   MASTER / "04_SYSTEM_UICONS" / "lightning.svg",
    "ic_play_button": MASTER / "04_SYSTEM_UICONS" / "play_button.svg",
    "ic_search":      MASTER / "04_SYSTEM_UICONS" / "search.svg",
    "ic_share":       MASTER / "04_SYSTEM_UICONS" / "share.svg",
    "ic_sun":         MASTER / "04_SYSTEM_UICONS" / "sun.svg",
    "ic_upload":      MASTER / "04_SYSTEM_UICONS" / "upload.svg",
}

# ─── Remove list: drawable stems to delete entirely ──────────────────────────

REMOVE = [
    # black_only stubs — AI brand variants with no real art
    "chatgpt_v1","chatgpt_v3","claude_v4","copilot_v2","copilot_v3",
    "grok_v1","grok_v2","grok_v3","grok_v4","notion_v1",
    # empty core icons with no source SVG anywhere
    "ic_ai_agent_network","ic_ai_data_processing","ic_ai_model","ic_ai_pipeline","ic_ai_swarm",
    "ic_bicycle","ic_bug_virus","ic_capacitor","ic_chart_pie","ic_clock_time","ic_coins_finance",
    "ic_community","ic_diamond_premium","ic_diode","ic_equalizer","ic_followers",
    "ic_hashtag","ic_mountain","ic_navigation_arrow","ic_neural_network",
    "ic_package_box","ic_pin_thumbtack","ic_pulse_heartbeat","ic_resistor",
    "ic_running_person","ic_settings_slider","ic_shopping_cart","ic_snowflake",
    "ic_target_goal","ic_transistor","ic_tree","ic_verified_badge","ic_vinyl_record",
    "ic_wheelchair","ic_yoga_meditation",
]

def strip_appfilter_xml(xml_path, remove_stems):
    """Remove <item> entries for deleted drawables from an appfilter.xml."""
    if not xml_path.exists():
        return 0
    text = xml_path.read_text(encoding="utf-8")
    removed = 0
    for stem in remove_stems:
        # Match: drawable="stem" anywhere in an <item .../> line
        new_text, n = re.subn(
            rf'\n[ \t]*<item[^>]+drawable="{re.escape(stem)}"[^/]*/>', '', text
        )
        if n == 0:
            new_text, n = re.subn(
                rf'[ \t]*<item[^>]+drawable="{re.escape(stem)}"[^/]*/>[ \t]*\n', '', text
            )
        if n > 0:
            text = new_text
            removed += n
    xml_path.write_text(text, encoding="utf-8")
    return removed

def strip_icon_array(xml_path, remove_stems):
    """Remove <item>stem</item> entries from icon_pack.xml drawable array."""
    if not xml_path.exists():
        return 0
    text = xml_path.read_text(encoding="utf-8")
    removed = 0
    for stem in remove_stems:
        new_text, n = re.subn(
            rf'\n[ \t]*<item>{re.escape(stem)}</item>', '', text
        )
        if n == 0:
            new_text, n = re.subn(
                rf'[ \t]*<item>{re.escape(stem)}</item>[ \t]*\n', '', text
            )
        if n > 0:
            text = new_text
            removed += n
    xml_path.write_text(text, encoding="utf-8")
    return removed

def main():
    drawable_dir = RES / "drawable-nodpi"
    nodpi_dir = RES / "drawable-nodpi"
    icon_array_xml = RES / "xml" / "icon_pack.xml"
    appfilter_xml = RES / "xml" / "appfilter.xml"
    appfilter_raw = RES / "raw" / "appfilter.xml"
    appfilter_assets = ANDROID / ".." / "assets" / "appfilter.xml"  # app/assets/

    # 1. Fix: regenerate from source SVGs
    fixed = 0
    for stem, src in FIXABLE.items():
        if not src.exists():
            print(f"  WARN: source missing for {stem}: {src}")
            continue
        vector = convert_svg(src)
        # Validate — must produce at least one path
        test_lines = [l for l in vector.splitlines() if "<path" in l]
        if not test_lines:
            print(f"  WARN: conversion produced no paths for {stem}, will remove instead")
            REMOVE.append(stem)
            continue
        for target_dir in (nodpi_dir,):
            (target_dir / f"{stem}.xml").write_text(vector, encoding="utf-8")
        print(f"  FIXED: {stem}  ({len(test_lines)} path(s))")
        fixed += 1

    # 2. Remove: delete drawable files + strip from XMLs
    deleted_files = 0
    for stem in REMOVE:
        for d in (drawable_dir, nodpi_dir):
            f = d / f"{stem}.xml"
            if f.exists():
                f.unlink()
                deleted_files += 1

    # Strip from icon array and appfilter copies
    array_removed = strip_icon_array(icon_array_xml, REMOVE)
    af_xml = strip_appfilter_xml(appfilter_xml, REMOVE)
    af_raw = strip_appfilter_xml(appfilter_raw, REMOVE)
    af_assets = strip_appfilter_xml(appfilter_assets, REMOVE)

    print(f"\nSummary:")
    print(f"  Fixed (regenerated):  {fixed}")
    print(f"  Deleted files:        {deleted_files}")
    print(f"  icon_pack.xml items removed:  {array_removed}")
    print(f"  appfilter.xml entries removed: xml={af_xml} raw={af_raw} assets={af_assets}")
    print(f"  Net drawable count: was 856, now {856 + fixed - len(REMOVE)}")

if __name__ == "__main__":
    main()
