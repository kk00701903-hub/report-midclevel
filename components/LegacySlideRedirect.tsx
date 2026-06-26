"use client";

import { useEffect } from "react";
import { getBasePath } from "@/lib/basePath";

type LegacySlideRedirectProps = {
  targetSlideId: number;
};

export default function LegacySlideRedirect({ targetSlideId }: LegacySlideRedirectProps) {
  useEffect(() => {
    const basePath = getBasePath();
    window.location.replace(`${basePath}/slides/${targetSlideId}/`);
  }, [targetSlideId]);

  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        background: "#141414",
        color: "#94A3B8",
        fontFamily: '"Noto Sans KR", sans-serif',
      }}
    >
      슬라이드 {targetSlideId}로 이동 중…
    </div>
  );
}
