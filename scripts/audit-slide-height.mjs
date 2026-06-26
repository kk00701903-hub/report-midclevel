import { chromium } from "playwright";
import { readFileSync, writeFileSync } from "fs";
import { join, resolve } from "path";

const slidesDir = resolve(process.argv[2] ?? join(process.cwd(), "public", "slides"));
const outPath = process.argv[3] ?? "slide-audit.json";

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage();
await page.setViewportSize({ width: 960, height: 720 });

const results = [];
for (let i = 1; i <= 37; i++) {
  const filePath = join(slidesDir, `${i}.html`);
  try {
    const html = readFileSync(filePath, "utf8");
    await page.setContent(html, { waitUntil: "networkidle", timeout: 30000 });
    await page.waitForTimeout(200);
    const info = await page.evaluate(() => {
      const root = document.querySelector("body > div");
      if (!root) return { error: "no root" };
      const rect = root.getBoundingClientRect();
      return {
        scrollHeight: root.scrollHeight,
        clientHeight: root.clientHeight,
        offsetHeight: root.offsetHeight,
        height: rect.height,
        overflow: root.scrollHeight > 720,
      };
    });
    results.push({ slide: i, file: filePath, ...info });
  } catch (e) {
    results.push({ slide: i, file: filePath, error: String(e) });
  }
}

await browser.close();
writeFileSync(outPath, JSON.stringify(results, null, 2));
const overflow = results.filter((r) => r.overflow);
console.log(`Checked ${results.length} slides, overflow: ${overflow.length}`);
overflow.forEach((r) => console.log(`  slide ${r.slide}: scrollHeight=${r.scrollHeight}`));
