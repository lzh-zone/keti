const { chromium } = require('playwright');
(async () => {
    const browser = await chromium.launch({
        executablePath: 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
        headless: true
    });
    const page = await browser.newPage({ viewport: { width: 375, height: 812 }, isMobile: true });
    await page.goto('http://localhost:8000/6.recruit_students.html');
    const info = await page.evaluate(() => {
        const img = document.querySelector('img[src*="join_us"]');
        const right = document.querySelector('.right');
        const main = document.querySelector('.main_content');
        const content = document.querySelector('.content');
        const getB = el => el ? {
            tag: el.tagName,
            cls: el.className,
            w: Math.round(el.getBoundingClientRect().width),
            h: Math.round(el.getBoundingClientRect().height),
            l: Math.round(el.getBoundingClientRect().left),
            cssW: getComputedStyle(el).width,
            cssH: getComputedStyle(el).height,
            cssMaxW: getComputedStyle(el).maxWidth,
            pos: getComputedStyle(el).position
        } : null;
        return { img: getB(img), right: getB(right), main: getB(main), content: getB(content) };
    });
    console.log(JSON.stringify(info, null, 2));
    await browser.close();
})();
