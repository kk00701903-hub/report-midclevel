#!/usr/bin/env python3
"""Apply Microsoft Fluent Dark theme to all slide HTML files."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLIDES_DIR = ROOT / "public" / "slides"
THEME_HREF = "/report-midclevel/slides/shared/slide-theme-fluent-dark.css"
THEME_LINK = f'<link rel="stylesheet" href="{THEME_HREF}">'

# Hardcoded color replacements (order matters for longer patterns first)
HEX_REPLACEMENTS: list[tuple[str, str]] = [
    ("#0A0E1A", "var(--ppt-bg)"),
    ("#0a0e1a", "var(--ppt-bg)"),
    ("#141B2D", "var(--ppt-bg-soft)"),
    ("#141b2d", "var(--ppt-bg-soft)"),
    ("#1E2638", "var(--ppt-surface)"),
    ("#1e2638", "var(--ppt-surface)"),
    ("#2A344A", "var(--ppt-surface-2)"),
    ("#2a344a", "var(--ppt-surface-2)"),
    ("#334155", "var(--ppt-border)"),
    ("#00F0FF", "var(--ppt-accent)"),
    ("#00f0ff", "var(--ppt-accent)"),
    ("#FACC15", "var(--ppt-accent-2)"),
    ("#facc15", "var(--ppt-accent-2)"),
    ("#22C55E", "var(--ppt-good)"),
    ("#22c55e", "var(--ppt-good)"),
    ("#94A3B8", "var(--ppt-text-2)"),
    ("#94a3b8", "var(--ppt-text-2)"),
    ("#64748B", "var(--ppt-text-3)"),
    ("#64748b", "var(--ppt-text-3)"),
    ("#0B1D3A", "var(--ppt-bg)"),
    ("#122849", "var(--ppt-bg-soft)"),
    ("#1A3560", "var(--ppt-surface)"),
    ("#2563EB", "var(--ppt-accent)"),
    ("#3B82F6", "var(--ppt-accent)"),
    ("#60A5FA", "var(--ppt-accent-light)"),
    ("#E2E8F0", "var(--ppt-text-2)"),
    ("#F59E0B", "var(--ppt-warn)"),
    ("#A78BFA", "var(--ppt-purple)"),
    ("#FB923C", "var(--ppt-orange)"),
    ("#8B5CF6", "var(--ppt-chart-4)"),
]

RGBA_REPLACEMENTS: list[tuple[str, str]] = [
    ("rgba(0, 240, 255,", "rgba(0, 120, 212,"),
    ("rgba(0,240,255,", "rgba(0, 120, 212,"),
    ("rgba(250, 204, 21,", "rgba(255, 185, 0,"),
    ("rgba(250,204,21,", "rgba(255, 185, 0,"),
    ("rgba(10, 14, 26,", "rgba(20, 20, 20,"),
    ("rgba(10,14,26,", "rgba(20, 20, 20,"),
    ("rgba(37,99,235,", "rgba(0, 120, 212,"),
    ("rgba(37, 99, 235,", "rgba(0, 120, 212,"),
    ("rgba(96,165,250,", "rgba(80, 230, 255,"),
]

ROOT_BLOCK_RE = re.compile(r":root\s*\{[^}]*\}", re.DOTALL | re.IGNORECASE)


def strip_root_blocks(text: str) -> str:
    """Remove inline :root variable blocks; theme CSS is the single source."""
    prev = None
    while prev != text:
        prev = text
        text = ROOT_BLOCK_RE.sub("", text)
    return text


def inject_theme_link(text: str) -> str:
    if THEME_HREF in text:
        return text
    marker = 'href="/report-midclevel/slides/shared/slide-motion.css">'
    alt = 'href="/report_fassmid/slides/shared/slide-motion.css">'
    if marker in text:
        return text.replace(marker, marker + "\n" + THEME_LINK, 1)
    if alt in text:
        new_marker = alt + "\n" + THEME_LINK.replace("/report-midclevel/", "/report_fassmid/")
        return text.replace(alt, new_marker, 1)
    # fallback: after motion.css any path
    m = re.search(r'(<link rel="stylesheet" href="[^"]*slide-motion\.css">)', text)
    if m:
        return text.replace(m.group(1), m.group(1) + "\n" + THEME_LINK, 1)
    return text


def apply_replacements(text: str) -> str:
    for old, new in HEX_REPLACEMENTS:
        text = text.replace(old, new)
    for old, new in RGBA_REPLACEMENTS:
        text = text.replace(old, new)
    # body background hardcoded
    text = re.sub(
        r"background-color:\s*var\(--ppt-bg\);\s*display:\s*flex",
        "background-color: var(--ppt-bg); display: flex",
        text,
    )
    text = re.sub(
        r"background:\s*#141414;",
        "background: var(--ppt-bg);",
        text,
    )
    return text


def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    text = original
    text = inject_theme_link(text)
    text = strip_root_blocks(text)
    text = apply_replacements(text)
    if text != original:
        path.write_text(text, encoding="utf-8")
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
