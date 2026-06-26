"""Insert 4 CEO architecture primer slides after slide 5."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLIDES_DIR = ROOT / "public" / "slides"
INSERT_AT = 6
COUNT = 4
SOURCES = [
    ROOT / "scripts" / "_arch_slide_06.html",
    ROOT / "scripts" / "_arch_slide_07.html",
    ROOT / "scripts" / "_arch_slide_08.html",
    ROOT / "scripts" / "_arch_slide_09.html",
]
NEW_TITLES = [
    "아키텍처의 이해 — Web · WAS · DB란?",
    "시스템 3대 핵심 요소",
    "차세대 3계층 구조 — 왜 분리하나?",
    "레거시 탈피 — 모듈형으로 전환",
]


def shift_files_up(from_id: int, delta: int) -> None:
    ids = sorted(int(p.stem) for p in SLIDES_DIR.glob("*.html"))
    for i in reversed(ids):
        if i < from_id:
            continue
        src = SLIDES_DIR / f"{i}.html"
        dst = SLIDES_DIR / f"{i + delta}.html"
        if src.exists():
            src.rename(dst)


def insert_new_slides() -> None:
    shift_files_up(INSERT_AT, COUNT)
    for offset, src in enumerate(SOURCES):
        (SLIDES_DIR / f"{INSERT_AT + offset}.html").write_bytes(src.read_bytes())


def parse_titles() -> list[str]:
    text = (ROOT / "lib" / "slides.ts").read_text(encoding="utf-8")
    return re.findall(r'\{ id: \d+, title: "([^"]*)" \}', text)


def write_slides_ts(titles: list[str]) -> None:
    lines = [
        "export type Slide = {",
        "  id: number;",
        "  title: string;",
        "};",
        "",
        f"export const SLIDE_COUNT = {len(titles)};",
        "",
        "export const SLIDES: Slide[] = [",
    ]
    for i, title in enumerate(titles, start=1):
        esc = title.replace("\\", "\\\\").replace('"', '\\"')
        lines.append(f'  {{ id: {i}, title: "{esc}" }},')
    lines.extend(
        [
            "];",
            "",
            "export function getSlideById(id: number): Slide | undefined {",
            "  return SLIDES.find((slide) => slide.id === id);",
            "}",
            "",
            "export function isValidSlideId(id: number): boolean {",
            "  return id >= 1 && id <= SLIDE_COUNT;",
            "}",
            "",
        ]
    )
    (ROOT / "lib" / "slides.ts").write_text("\n".join(lines), encoding="utf-8")


def bump_slide_details(from_id: int, delta: int) -> None:
    path = ROOT / "lib" / "slideDetails.ts"
    text = path.read_text(encoding="utf-8")
    ids = sorted({int(m.group(1)) for m in re.finditer(r"slideId: (\d+),", text)}, reverse=True)
    for i in ids:
        if i >= from_id:
            text = text.replace(f"slideId: {i},", f"slideId: {i + delta},")
    path.write_text(text, encoding="utf-8")


def update_slide_parts() -> None:
    path = ROOT / "lib" / "slideParts.ts"
    text = path.read_text(encoding="utf-8")
    replacements = {
        "endSlideId: 6,": "endSlideId: 10,",
        "startSlideId: 7,\n    endSlideId: 14,": "startSlideId: 11,\n    endSlideId: 18,",
        "startSlideId: 15,\n    endSlideId: 19,": "startSlideId: 19,\n    endSlideId: 23,",
        "startSlideId: 20,\n    endSlideId: 28,": "startSlideId: 24,\n    endSlideId: 32,",
        "startSlideId: 29,\n    endSlideId: 33,": "startSlideId: 33,\n    endSlideId: 37,",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


def update_part1_divider() -> None:
    path = SLIDES_DIR / "2.html"
    text = path.read_text(encoding="utf-8")
    insert_block = """    <div class="section-topic-item">
      <div class="topic-dot"></div>
      <span class="topic-text">아키텍처의 이해 — Web · WAS · DB · 3계층 구조</span>
    </div>
"""
    marker = '      <span class="topic-text">Executive Summary - FaSS 플랫폼 구축</span>'
    if "아키텍처의 이해" not in text:
        text = text.replace(
            '    <div class="section-topic-item">\n      <div class="topic-dot"></div>\n' + marker,
            insert_block + '    <div class="section-topic-item">\n      <div class="topic-dot"></div>\n' + marker,
        )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    titles = parse_titles()
    insert_idx = INSERT_AT - 1  # after slide 5 -> index 5
    for t in reversed(NEW_TITLES):
        titles.insert(insert_idx, t)
    insert_new_slides()
    write_slides_ts(titles)
    bump_slide_details(INSERT_AT, COUNT)
    update_slide_parts()
    update_part1_divider()
    print(f"Inserted {COUNT} slides at {INSERT_AT}. SLIDE_COUNT={len(titles)}")


if __name__ == "__main__":
    main()
