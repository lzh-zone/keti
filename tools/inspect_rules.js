const { chromium } = require('playwright');
(async () => {
    const browser = await chromium.launch({
        executablePath: 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
        headless: true
    });
    const page = await browser.newPage({ viewport: { width: 375, height: 812 }, isMobile: true });
    await page.goto('http://localhost:8000/6.recruit_students.html');
    const matched = await page.evaluate(() => {
        const img = document.querySelector('img[src*="join_us"]');
        const res = [];
        for (let s of document.styleSheets) {
            try {
                for (let r of s.cssRules) {
                    if (r.selectorText && img.matches(r.selectorText)) {
                        res.push({ sel: r.selectorText, css: r.cssText });
                    }
                    if (r.cssRules) {
                        for (let sub of r.cssRules) {
                            if (sub.selectorText && img.matches(sub.selectorText)) {
                                res.push({ sel: sub.selectorText, css: sub.cssText, media: r.conditionText });
                            }
                        }
                    }
                }
            } catch(e) {}
        }
        return res;
    });
    console.log(JSON.stringify(matched, null, 2));
    await browser.close();
})();
