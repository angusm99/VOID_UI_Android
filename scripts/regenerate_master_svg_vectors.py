import math
import re
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(r"C:\Users\User\CLAUDE\VOID_UI")
MASTER = ROOT / "01_ICON_PACK_MASTER" / "ICON_MASTER"
ANDROID = ROOT / "02_ANDROID_ICON_PACK_APP" / "VOID_UI_Android" / "app" / "src" / "main" / "res"

CATEGORIES = {
    "06_TERMINAL": "terminal_",
    "07_CRICKET_NATIONS": "nation_",
    "08_SPORTS_ZONES": "sports_",
    "09_XENOCOMM": "xeno_",
}

COLOR_MAP = {
    "black": "#FF000000",
    "white": "#FFFFFFFF",
    "#fff": "#FFFFFFFF",
    "#ffffff": "#FFFFFFFF",
    "#000": "#FF000000",
    "#000000": "#FF000000",
    "ZONE_PRIMARY": "#FF00FFFF",
    "ZONE_SECONDARY": "#FFFF007F",
    "ZONE_ACCENT": "#FFFFFFFF",
    "currentcolor": "#FFFFFFFF",
    "currentColor": "#FFFFFFFF",
}


def clean_number(value):
    number = float(value)
    if abs(number - round(number)) < 0.000001:
        return str(int(round(number)))
    return f"{number:.3f}".rstrip("0").rstrip(".")


def attr_float(attrs, name, default=0):
    raw = attrs.get(name)
    if raw is None:
        return default
    return float(str(raw).replace("px", ""))


def android_color(value):
    if value is None or value == "" or value == "none":
        return None
    if value in COLOR_MAP:
        return COLOR_MAP[value]
    lowered = value.lower()
    if lowered in COLOR_MAP:
        return COLOR_MAP[lowered]
    if lowered.startswith("#"):
        hex_value = lowered[1:]
        if len(hex_value) == 3:
            hex_value = "".join(ch * 2 for ch in hex_value)
        if len(hex_value) == 6:
            return "#FF" + hex_value.upper()
        if len(hex_value) == 8:
            return "#" + hex_value.upper()
    return value


def alpha(attrs, kind):
    values = []
    if "opacity" in attrs:
        values.append(float(attrs["opacity"]))
    key = f"{kind}-opacity"
    if key in attrs:
        values.append(float(attrs[key]))
    if not values:
        return None
    result = 1.0
    for value in values:
        result *= value
    return clean_number(result)


def parse_style(style):
    result = {}
    if not style:
        return result
    for part in style.split(";"):
        if ":" not in part:
            continue
        key, value = part.split(":", 1)
        result[key.strip()] = value.strip()
    return result


def parse_translate(transform):
    if not transform:
        return 0.0, 0.0
    match = re.search(r"translate\(([^,\s)]+)[,\s]+([^,\s)]+)\)", transform)
    if not match:
        match = re.search(r"translate\(([^,\s)]+)\)", transform)
        if not match:
            return 0.0, 0.0
        return float(match.group(1)), 0.0
    return float(match.group(1)), float(match.group(2))


def local_name(tag):
    return tag.split("}", 1)[-1]


def inherited_attrs(parent, element):
    attrs = dict(parent)
    attrs.update(parse_style(element.attrib.get("style")))
    for key, value in element.attrib.items():
        if key != "style":
            attrs[key] = value
    return attrs


def circle_path(cx, cy, radius):
    x1 = clean_number(cx - radius)
    x2 = clean_number(cx + radius)
    y = clean_number(cy)
    r = clean_number(radius)
    return f"M{x1},{y} A{r},{r} 0,1 0 {x2},{y} A{r},{r} 0,1 0 {x1},{y}"


def rect_path(x, y, width, height, rx=0):
    x2 = x + width
    y2 = y + height
    if rx <= 0:
        return f"M{clean_number(x)},{clean_number(y)} H{clean_number(x2)} V{clean_number(y2)} H{clean_number(x)} Z"
    rx = min(rx, width / 2, height / 2)
    return (
        f"M{clean_number(x + rx)},{clean_number(y)} "
        f"H{clean_number(x2 - rx)} Q{clean_number(x2)},{clean_number(y)} {clean_number(x2)},{clean_number(y + rx)} "
        f"V{clean_number(y2 - rx)} Q{clean_number(x2)},{clean_number(y2)} {clean_number(x2 - rx)},{clean_number(y2)} "
        f"H{clean_number(x + rx)} Q{clean_number(x)},{clean_number(y2)} {clean_number(x)},{clean_number(y2 - rx)} "
        f"V{clean_number(y + rx)} Q{clean_number(x)},{clean_number(y)} {clean_number(x + rx)},{clean_number(y)} Z"
    )


def points_path(points, close):
    coords = [float(value) for value in re.findall(r"-?\d+(?:\.\d+)?", points or "")]
    if len(coords) < 4:
        return None
    pairs = list(zip(coords[0::2], coords[1::2]))
    commands = [f"M{clean_number(pairs[0][0])},{clean_number(pairs[0][1])}"]
    commands.extend(f"L{clean_number(x)},{clean_number(y)}" for x, y in pairs[1:])
    if close:
        commands.append("Z")
    return " ".join(commands)


def path_style(attrs):
    fill = android_color(attrs.get("fill", "none"))
    stroke = android_color(attrs.get("stroke"))
    values = []
    if fill:
        values.append(("android:fillColor", fill))
        fill_alpha = alpha(attrs, "fill")
        if fill_alpha is not None:
            values.append(("android:fillAlpha", fill_alpha))
    if stroke:
        values.append(("android:strokeColor", stroke))
        values.append(("android:strokeWidth", clean_number(attr_float(attrs, "stroke-width", 1))))
        if "stroke-linecap" in attrs:
            values.append(("android:strokeLineCap", attrs["stroke-linecap"]))
        if "stroke-linejoin" in attrs:
            values.append(("android:strokeLineJoin", attrs["stroke-linejoin"]))
        stroke_alpha = alpha(attrs, "stroke")
        if stroke_alpha is not None:
            values.append(("android:strokeAlpha", stroke_alpha))
    return values


def emit_path(path_data, attrs):
    if not path_data:
        return []
    style = path_style(attrs)
    if not style:
        style = [("android:fillColor", "#00000000")]
    lines = ["    <path"]
    for key, value in style:
        lines.append(f'        {key}="{value}"')
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
        x1 = attr_float(attrs, "x1") + tx
        y1 = attr_float(attrs, "y1") + ty
        x2 = attr_float(attrs, "x2") + tx
        y2 = attr_float(attrs, "y2") + ty
        paths.extend(emit_path(f"M{clean_number(x1)},{clean_number(y1)} L{clean_number(x2)},{clean_number(y2)}", attrs))
    elif tag == "circle":
        cx = attr_float(attrs, "cx") + tx
        cy = attr_float(attrs, "cy") + ty
        paths.extend(emit_path(circle_path(cx, cy, attr_float(attrs, "r")), attrs))
    elif tag == "rect":
        x = attr_float(attrs, "x") + tx
        y = attr_float(attrs, "y") + ty
        paths.extend(emit_path(rect_path(x, y, attr_float(attrs, "width"), attr_float(attrs, "height"), attr_float(attrs, "rx")), attrs))
    elif tag == "polyline":
        paths.extend(emit_path(points_path(attrs.get("points"), False), attrs))
    elif tag == "polygon":
        paths.extend(emit_path(points_path(attrs.get("points"), True), attrs))

    for child in element:
        paths.extend(collect_paths(child, attrs, tx, ty))
    return paths


def convert(svg_path):
    tree = ET.parse(svg_path)
    root = tree.getroot()
    view_box = root.attrib.get("viewBox", "0 0 512 512").split()
    viewport_width = view_box[2] if len(view_box) == 4 else "512"
    viewport_height = view_box[3] if len(view_box) == 4 else "512"
    paths = collect_paths(root, {})
    return "\n".join([
        '<vector xmlns:android="http://schemas.android.com/apk/res/android"',
        '    android:width="512dp"',
        '    android:height="512dp"',
        f'    android:viewportWidth="{viewport_width}"',
        f'    android:viewportHeight="{viewport_height}">',
        *paths,
        '</vector>',
        '',
    ])


def main():
    converted = 0
    for folder, prefix in CATEGORIES.items():
        source_dir = MASTER / folder
        for svg_path in sorted(source_dir.glob(f"{prefix}*.svg")):
            vector = convert(svg_path)
            for target_root in (ANDROID / "drawable", ANDROID / "drawable-nodpi"):
                (target_root / f"{svg_path.stem}.xml").write_text(vector, encoding="utf-8")
            converted += 1
    print(f"Regenerated {converted} SVGs into drawable and drawable-nodpi")


if __name__ == "__main__":
    main()
