#!/usr/bin/env python3
"""Switch slides to Microsoft Fluent Light theme and fix dark-only hardcoded colors."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLIDES_DIR = ROOT / "public" / "slides"
DARK_HREF = "/report-midclevel/slides/shared/slide-theme-fluent-dark.css"
LIGHT_HREF = "/report-midclevel/slides/shared/slide-theme-fluent-light.css"

# rgba(255,255,255,...) patterns for progress tracks etc.
WHITE_RGBA_RE = re.compile(
    r"rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*([\d.]+)\s*\)",
    re.IGNORECASE,
)


def replace_white_rgba(match: re.Match[str]) -> str:
    alpha = float(match.group(1))
    if alpha <= 0.05:
        return "var(--ppt-track-bg)"
    if alpha <= 0.12:
        return "var(--ppt-track-bg)"
    return "rgba(0, 0, 0, 0.08)"


def process_text(text: str) -> str:
    text = text.replace(DARK_HREF, LIGHT_HREF)
    text = text.replace(
        "/report_fassmid/slides/shared/slide-theme-fluent-dark.css",
        "/report_fassmid/slides/shared/slide-theme-fluent-light.css",
    )

    # Dark overlay gradients → light overlay
    text = text.replace(
        "rgba(20, 20, 20, 0.95)",
        "rgba(255, 255, 255, 0.92)",
    )
    text = text.replace(
        "rgba(20, 20, 20, 0.7)",
        "rgba(255, 255, 255, 0.75)",
    )
    text = text.replace("rgba(20,20,20,0.95)", "rgba(255,255,255,0.92)")
    text = text.replace("rgba(20,20,20,0.7)", "rgba(255,255,255,0.75)")
    text = text.replace(
        "rgba(20, 27, 45, 0.6)",
        "rgba(243, 242, 241, 0.95)",
    )
    text = text.replace("rgba(20,27,45,.6)", "rgba(243,242,241,.95)")
    text = text.replace(
        "linear-gradient(135deg,rgba(31,31,31,.95),rgba(20,20,20,.85))",
        "linear-gradient(135deg,rgba(255,255,255,.98),rgba(243,242,241,.95))",
    )
    text = text.replace(
        "linear-gradient(135deg,rgba(20,27,45,.92),rgba(20, 20, 20,.75))",
        "linear-gradient(135deg,rgba(255,255,255,.98),rgba(243,242,241,.92))",
    )
    text = text.replace(
        "background-color: rgba(30, 38, 56, 0.6)",
        "background-color: var(--ppt-bg-soft)",
    )
    text = text.replace(
        "background-color:rgba(30,38,56,0.6)",
        "background-color:var(--ppt-bg-soft)",
    )

    # Inline white text on light bg (not on colored badges)
    text = re.sub(
        r"color:\s*#fff\b",
        "color:var(--ppt-text-1)",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"color:\s*#FFF\b",
        "color:var(--ppt-text-1)",
        text,
    )
    text = re.sub(
        r'style="color:#fff"',
        'style="color:var(--ppt-text-1)"',
        text,
        flags=re.IGNORECASE,
    )

    text = WHITE_RGBA_RE.sub(replace_white_rgba, text)

    return text


def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = process_text(original)
    if updated != original:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = 0
    for html in sorted(SLIDES_DIR.glob("*.html")):
        if process_file(html):
            changed += 1
            print(f"  updated {html.name}")
    print(f"Done: {changed} slide(s) updated.")


if __name__ == "__main__":
    main()
