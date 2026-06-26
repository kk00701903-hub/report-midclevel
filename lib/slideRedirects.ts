/**
 * 구버전(최대 36장) 슬라이드 번호 → 현재 슬라이드 ID.
 * 북마크·공유 URL 호환용.
 * 현재 유효한 슬라이드 ID(1–37)는 포함하지 않습니다.
 * 아키텍처 4장(6–9) 삽입으로 6번 이후 슬라이드가 +4 이동한 것을 반영합니다.
 */
export const LEGACY_SLIDE_REDIRECTS: Record<number, number> = {
  10: 16,
  11: 17,
  12: 18,
  13: 19,
  14: 20,
  15: 21,
  16: 22, // PART 4 간지 (구 16p)
  17: 23,
  18: 24,
  19: 25, // PART 4 간지 (구 19p)
  20: 26,
  21: 27,
  22: 28,
  23: 29,
  24: 30,
  25: 31,
  26: 32,
  27: 12,
  28: 13,
  33: 12, // 스프린트 운영현황 (구 덱)
  34: 25, // 비즈니스 혁신1
  35: 34, // 롤아웃 로드맵
  36: 37, // 맺음말
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
