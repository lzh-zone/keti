const { chromium } = require('playwright');

(async () => {
    try {
        const browser = await chromium.launch({
            executablePath: "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
            headless: true
        });
        const context = await browser.newContext({
            viewport: { width: 375, height: 812 },
            isMobile: true,
            hasTouch: true
        });
        const page = await context.newPage();
        await page.goto('http://localhost:8000/4.1.2026.html', { waitUntil: 'networkidle' });
        await page.screenshot({ path: 'C:\\Users\\24415\\.gemini\\antigravity\\scratch\\shot_playwright_mobile.png' });
        
        // Also evaluate any elements that overflow 375px
        const overflows = await page.evaluate(() => {
            const list = [];
            document.querySelectorAll('*').forEach(el => {
                const r = el.getBoundingClientRect();
                if (r.right > 376 || r.width > 376) {
                    list.push({
                        tag: el.tagName,
                        cls: el.className,
                        w: Math.round(r.width),
                        r: Math.round(r.right),
                        l: Math.round(r.left)
                    });
                }
            });
            return list;
        });

        console.log('Overflow count on real mobile viewport:', overflows.length);
        if (overflows.length > 0) {
            console.log('Overflow elements:', JSON.stringify(overflows.slice(0, 10), null, 2));
        }
        await browser.close();
        console.log('DONE');
    } catch (e) {
        console.error('ERROR:', e);
    }
})();
