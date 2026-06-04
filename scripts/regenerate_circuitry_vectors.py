from __future__ import annotations

import json
from pathlib import Path
import xml.etree.ElementTree as ET


ACCENT = "#FF00FF41"
TRANSPARENT = "@android:color/transparent"
STROKE_WIDTH = "14"
LINE_CAP = "round"
LINE_JOIN = "round"


def fmt(value: str | float | int) -> str:
    return f"{float(value):g}"


def circle_path(cx: str, cy: str, r: str) -> str:
    cx_f = fmt(cx)
    cy_f = fmt(cy)
    r_f = fmt(r)
    left = fmt(float(cx) - float(r))
    right = fmt(float(cx) + float(r))
    return (
        f"M{left} {cy_f} "
        f"A{r_f} {r_f} 0 1 0 {right} {cy_f} "
        f"A{r_f} {r_f} 0 1 0 {left} {cy_f} Z"
    )


def ellipse_path(cx: str, cy: str, rx: str, ry: str) -> str:
    cx_f = fmt(cx)
    cy_f = fmt(cy)
    rx_f = fmt(rx)
    ry_f = fmt(ry)
    left = fmt(float(cx) - float(rx))
    right = fmt(float(cx) + float(rx))
    return (
        f"M{left} {cy_f} "
        f"A{rx_f} {ry_f} 0 1 0 {right} {cy_f} "
        f"A{rx_f} {ry_f} 0 1 0 {left} {cy_f} Z"
    )


def rect_path(x: str, y: str, width: str, height: str, rx: str | None) -> str:
    x_f = float(x)
    y_f = float(y)
    w_f = float(width)
    h_f = float(height)
    rx_f = float(rx or 0)
    rx_f = min(rx_f, w_f / 2, h_f / 2)

    left = fmt(x_f)
    top = fmt(y_f)
    right = fmt(x_f + w_f)
    bottom = fmt(y_f + h_f)

    if rx_f == 0:
        return f"M{left} {top} H{right} V{bottom} H{left} Z"

    r = fmt(rx_f)
    left_r = fmt(x_f + rx_f)
    right_r = fmt(x_f + w_f - rx_f)
    top_r = fmt(y_f + rx_f)
    bottom_r = fmt(y_f + h_f - rx_f)

    return (
        f"M{left_r} {top} "
        f"H{right_r} "
        f"A{r} {r} 0 0 1 {right} {top_r} "
        f"V{bottom_r} "
        f"A{r} {r} 0 0 1 {right_r} {bottom} "
        f"H{left_r} "
        f"A{r} {r} 0 0 1 {left} {bottom_r} "
        f"V{top_r} "
        f"A{r} {r} 0 0 1 {left_r} {top} Z"
    )


def points_path(points: str, close: bool) -> str:
    pairs = [segment.strip() for segment in points.split() if segment.strip()]
    coords = []
    for pair in pairs:
        x, y = pair.split(",")
        coords.append((fmt(x), fmt(y)))
    if not coords:
        raise ValueError("Empty points list")
    commands = [f"M{coords[0][0]} {coords[0][1]}"]
    commands.extend(f"L{x} {y}" for x, y in coords[1:])
    if close:
        commands.append("Z")
    return " ".join(commands)


def line_path(x1: str, y1: str, x2: str, y2: str) -> str:
    return f"M{fmt(x1)} {fmt(y1)} L{fmt(x2)} {fmt(y2)}"


def text_paths(text: str) -> list[dict[str, str]]:
    if text.strip().upper() != "AI":
        return []
    return [
        {
            "pathData": "M228 286 L246 226 L264 286 M236 264 L256 264",
            "fillColor": TRANSPARENT,
            "strokeColor": ACCENT,
            "strokeWidth": "12",
            "strokeLineCap": LINE_CAP,
            "strokeLineJoin": LINE_JOIN,
        },
        {
            "pathData": "M286 226 L314 226 M300 226 L300 286 M286 286 L314 286",
            "fillColor": TRANSPARENT,
            "strokeColor": ACCENT,
            "strokeWidth": "12",
            "strokeLineCap": LINE_CAP,
            "strokeLineJoin": LINE_JOIN,
        },
    ]


def style_for(node: ET.Element) -> tuple[str | None, str | None]:
    fill = node.attrib.get("fill")
    stroke = node.attrib.get("stroke")
    return fill, stroke


def vector_paths(inner_svg: str) -> list[dict[str, str]]:
    root = ET.fromstring(f"<root>{inner_svg}</root>")
    converted: list[dict[str, str]] = []

    for node in root:
        tag = node.tag.split("}")[-1]
        fill, stroke = style_for(node)

        fill_color = TRANSPARENT
        stroke_color = ACCENT
        stroke_width = STROKE_WIDTH
        stroke_line_cap = LINE_CAP
        stroke_line_join = LINE_JOIN

        if fill and fill.lower() != "none":
            fill_color = ACCENT
        if stroke == "none":
            stroke_color = None
        if stroke is None and fill_color == TRANSPARENT:
            stroke_color = ACCENT

        if tag == "path":
            path_data = node.attrib["d"]
        elif tag == "line":
            path_data = line_path(
                node.attrib["x1"], node.attrib["y1"], node.attrib["x2"], node.attrib["y2"]
            )
        elif tag == "circle":
            path_data = circle_path(node.attrib["cx"], node.attrib["cy"], node.attrib["r"])
        elif tag == "ellipse":
            path_data = ellipse_path(
                node.attrib["cx"], node.attrib["cy"], node.attrib["rx"], node.attrib["ry"]
            )
        elif tag == "rect":
            path_data = rect_path(
                node.attrib["x"],
                node.attrib["y"],
                node.attrib["width"],
                node.attrib["height"],
                node.attrib.get("rx"),
            )
        elif tag == "polygon":
            path_data = points_path(node.attrib["points"], close=True)
        elif tag == "polyline":
            path_data = points_path(node.attrib["points"], close=False)
        elif tag == "text":
            converted.extend(text_paths(node.text or ""))
            continue
        else:
            raise ValueError(f"Unsupported SVG element: {tag}")

        item = {
            "pathData": path_data,
            "fillColor": fill_color,
        }
        if stroke_color:
            item["strokeColor"] = stroke_color
            item["strokeWidth"] = stroke_width
            item["strokeLineCap"] = stroke_line_cap
            item["strokeLineJoin"] = stroke_line_join
        converted.append(item)

    return converted


def write_vector(path: Path, paths: list[dict[str, str]]) -> None:
    lines = [
        '<vector xmlns:android="http://schemas.android.com/apk/res/android"',
        '    android:width="512dp"',
        '    android:height="512dp"',
        '    android:viewportWidth="512"',
        '    android:viewportHeight="512">',
    ]
    for item in paths:
        lines.append("    <path")
        lines.append(f'        android:pathData="{item["pathData"]}"')
        lines.append(f'        android:fillColor="{item["fillColor"]}"')
        if "strokeColor" in item:
            lines.append(f'        android:strokeColor="{item["strokeColor"]}"')
            lines.append(f'        android:strokeWidth="{item["strokeWidth"]}"')
            lines.append(f'        android:strokeLineCap="{item["strokeLineCap"]}"')
            lines.append(f'        android:strokeLineJoin="{item["strokeLineJoin"]}"')
        lines.append("        />")
    lines.append("</vector>")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    workspace_root = Path(__file__).resolve().parents[3]
    source_json = workspace_root / "01_ICON_PACK_MASTER" / "ICON_MASTER" / "circuitry-paths.json"
    repo_root = Path(__file__).resolve().parents[1]
    destinations = [
        repo_root / "app" / "src" / "main" / "res" / "drawable",
        repo_root / "app" / "src" / "main" / "res" / "drawable-nodpi",
    ]

    data = json.loads(source_json.read_text(encoding="utf-8"))

    for name, inner_svg in data.items():
        paths = vector_paths(inner_svg)
        for dest in destinations:
            dest.mkdir(parents=True, exist_ok=True)
            write_vector(dest / f"circuitry_{name}.xml", paths)

    print(f"Regenerated {len(data)} circuitry vectors into {len(destinations)} resource folders.")


if __name__ == "__main__":
    main()
