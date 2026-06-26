/** 슬라이드 ID(내장 HTML 번호) 기준 PART 구간 정의 */

export type SlidePart = {
  partNumber: number;
  title: string;
};

export const SLIDE_PARTS: Array<SlidePart & { startSlideId: number; endSlideId: number }> = [
  {
    partNumber: 1,
    title: "전략적 비전 및 목표",
    startSlideId: 2,
    endSlideId: 10,
  },
  {
    partNumber: 2,
    title: "프로젝트 진행 경과 및 방향성",
    startSlideId: 11,
    endSlideId: 18,
  },
  {
    partNumber: 3,
    title: "기술 스택 및 아키텍처",
    startSlideId: 19,
    endSlideId: 23,
  },
  {
    partNumber: 4,
    title: "혁신 및 검증",
    startSlideId: 24,
    endSlideId: 32,
  },
  {
    partNumber: 5,
    title: "로드맵 및 미래 비전",
    startSlideId: 33,
    endSlideId: 37,
  },
];

/** PART 간지 슬라이드(목차 하이라이트용) */
export function isPartDividerTitle(title: string): boolean {
  return /^PART\s+\d+/i.test(title.trim());
}

/** 표지(1p) 등 PART 미표시 슬라이드 */
export function getSlidePart(builtinSlideId: number | null): SlidePart | null {
  if (builtinSlideId === null || builtinSlideId <= 1) return null;

  const part = SLIDE_PARTS.find(
    (p) => builtinSlideId >= p.startSlideId && builtinSlideId <= p.endSlideId,
  );

  if (!part) return null;

  return { partNumber: part.partNumber, title: part.title };
}

export function getBuiltinSlideIdFromFileName(fileName: string): number | null {
  const match = fileName.match(/^(\d+)\.html$/i);
  return match ? Number(match[1]) : null;
}
