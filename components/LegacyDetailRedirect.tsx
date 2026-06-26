"use client";

import { useEffect } from "react";
import { getBasePath } from "@/lib/basePath";

type LegacyDetailRedirectProps = {
  targetSlideId: number;
  detailId: string;
};

export default function LegacyDetailRedirect({ targetSlideId, detailId }: LegacyDetailRedirectProps) {
  useEffect(() => {
    const basePath = getBasePath();
    window.location.replace(`${basePath}/slides/${targetSlideId}/details/${detailId}/`);
  }, [targetSlideId, detailId]);

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
      상세 자료로 이동 중…
    </div>
  );
}
