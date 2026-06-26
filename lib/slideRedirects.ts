/**
 * 구버전 슬라이드 번호 → 현재 슬라이드 ID.
 * 북마크·공유 URL 호환용.
 * 현재 유효한 슬라이드 ID(1–37)는 포함하지 않습니다.
 */
export const LEGACY_SLIDE_REDIRECTS: Record<number, number> = {
  6: 10,
  7: 11,
  8: 12,
  9: 13,
  10: 14,
  11: 15,
  12: 16,
  13: 17,
  14: 18,
  15: 19,
  16: 20,
  17: 21,
  18: 22,
  19: 23,
  20: 24,
  21: 25,
  22: 26,
  23: 27,
  24: 28,
  25: 29,
  26: 30,
  27: 31,
  28: 32,
  29: 33,
  30: 34,
  31: 35,
  32: 36,
  33: 37,
  34: 25,
  35: 34,
  36: 37,
};

export function isLegacySlideId(slideId: number): boolean {
  return slideId in LEGACY_SLIDE_REDIRECTS;
}

export function resolveSlideId(slideId: number): number {
  return LEGACY_SLIDE_REDIRECTS[slideId] ?? slideId;
}

export function getLegacySlideIds(): number[] {
  return Object.keys(LEGACY_SLIDE_REDIRECTS).map(Number);
}

/** 구버전 슬라이드 번호용 상세 페이지 정적 경로 (대상 슬라이드의 detail 복제) */
export function getLegacyDetailParams(
  currentParams: { id: string; detailId: string }[],
): { id: string; detailId: string }[] {
  const legacy: { id: string; detailId: string }[] = [];
  for (const [legacyId, targetId] of Object.entries(LEGACY_SLIDE_REDIRECTS)) {
    for (const param of currentParams) {
      if (Number(param.id) === targetId) {
        legacy.push({ id: legacyId, detailId: param.detailId });
      }
    }
  }
  return legacy;
}
