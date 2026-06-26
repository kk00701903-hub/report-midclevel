export function getBasePath(): string {
  if (typeof window !== "undefined") {
    const match = window.location.pathname.match(/^(\/[^/]+)\/slides(?:\/|$)/);
    if (match) return match[1];
  }

  return process.env.NEXT_PUBLIC_BASE_PATH ?? "/report-midclevel";
}

export function getSlideHtmlUrl(fileName: string): string {
  const basePath = getBasePath();
  const path = `${basePath}/slides/${fileName}`;
  if (typeof window !== "undefined") {
    return new URL(path, window.location.origin).href;
  }
  return path;
}

/** 슬라이드 HTML·shared 에셋의 기준 URL (끝에 / 포함) */
export function getSlidesDirectoryUrl(): string {
  const basePath = getBasePath();
  const path = `${basePath}/slides/`;
  if (typeof window !== "undefined") {
    return new URL(path, window.location.origin).href;
  }
  return path;
}
