export type Slide = {
  id: number;
  title: string;
};

export const SLIDE_COUNT = 37;

export const SLIDES: Slide[] = [
  { id: 1, title: "(주)제때 차세대 FaSS 플랫폼 구축 중간 보고" },
  { id: 2, title: "PART 1 - 전략적 비전 및 목표" },
  { id: 3, title: "글로벌 디지털 4대 축" },
  { id: 4, title: "디지털 트렌드 — AI 디지털 워커 (AI Digital Worker)" },
  { id: 5, title: "FaSS 플랫폼 아이덴티티" },
  { id: 6, title: "아키텍처의 이해 — Web · WAS · DB란?" },
  { id: 7, title: "시스템 3대 핵심 요소" },
  { id: 8, title: "차세대 3계층 구조 — 왜 분리하나?" },
  { id: 9, title: "레거시 탈피 — 모듈형으로 전환" },
  { id: 10, title: "Executive Summary - FaSS 플랫폼 구축" },
  { id: 11, title: "PART 2 - 프로젝트 진행 경과 및 방향성" },
  { id: 12, title: "스프린트 운영현황" },
  { id: 13, title: "타사 프로젝트 비교" },
  { id: 14, title: "AI-Augmented 개발 워크플로우" },
  { id: 15, title: "프로젝트 진행경과 마일스톤" },
  { id: 16, title: "최적화 방안 1. AI 디지털 워커 활용" },
  { id: 17, title: "최적화 방안 2. 애자일 워룸 운영" },
  { id: 18, title: "최적화 방안 3. 사전 POC 운영" },
  { id: 19, title: "PART 3 - 기술 스택 및 아키텍처" },
  { id: 20, title: "핵심 기술 스택" },
  { id: 21, title: "아키텍처 원칙 1 — 안정적 시작, 점진적 확장" },
  { id: 22, title: "아키텍처 원칙 2 — 서비스 중단 없는 전환" },
  { id: 23, title: "아키텍처 원칙 3 — 자동화된 배포" },
  { id: 24, title: "PART 4 - 혁신 및 검증" },
  { id: 25, title: "비즈니스 혁신1: 차세대 영업 핵심 IT 엔진 보유" },
  { id: 26, title: "비즈니스 혁신2: AI 지능형 물류 플랫폼으로의 전환" },
  { id: 27, title: "비즈니스 혁신3: 전략적 수익화 IT 플랫폼 확보" },
  { id: 28, title: "비즈니스 혁신4 — 안전한 실전 검증 (JTGS)" },
  { id: 29, title: "비즈니스 혁신5 — 무결점 품질 통제" },
  { id: 30, title: "비즈니스 혁신6 — 클라우드 비용 최적화" },
  { id: 31, title: "비즈니스 혁신7 — AI 개발 자동화" },
  { id: 32, title: "비즈니스 혁신8: 빌더형 인재 육성을 위한 전환" },
  { id: 33, title: "PART 5 - 로드맵 및 미래 비전" },
  { id: 34, title: "단계적 롤아웃 로드맵" },
  { id: 35, title: "중장기 목표 1 — 자동 확장 인프라" },
  { id: 36, title: "중장기 목표 2 — 단계적 시스템 분리" },
  { id: 37, title: "맺음말" },
];

export function getSlideById(id: number): Slide | undefined {
  return SLIDES.find((slide) => slide.id === id);
}

export function isValidSlideId(id: number): boolean {
  return id >= 1 && id <= SLIDE_COUNT;
}
