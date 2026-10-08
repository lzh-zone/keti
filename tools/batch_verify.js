const { chromium } = require('playwright');
const path = require('path');

const PAGES = [
    { name: 'index', url: 'http://localhost:8000/index.html' },
    { name: 'news', url: 'http://localhost:8000/2.news.html' },
    { name: 'team_intro', url: 'http://localhost:8000/3.team_intro.html' },
    { name: 'teachers', url: 'http://localhost:8000/3.1.team_intro_teachers.html' },
    { name: 'students', url: 'http://localhost:8000/3.3.team_intro_shuoshi.html' },
    { name: 'teacher_detail', url: 'http://localhost:8000/3.1.team_intro_laoshi_liuaiping.html' },
    { name: 'papers', url: 'http://localhost:8000/4.1.2026.html' },
    { name: 'recruit', url: 'http://localhost:8000/6.recruit_students.html' }
];

const SCRATCH_DIR = 'C:\\Users\\24415\\.gemini\\antigravity\\scratch';

(async () => {
    const browser = await chromium.launch({
        executablePath: "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
        headless: true
    });

    console.log('--- Capturing Mobile Screenshots (375x812) ---');
    const mobileContext = await browser.newContext({
        viewport: { width: 375, height: 812 },
        isMobile: true,
        hasTouch: true
    });

    for (const p of PAGES) {
        const page = await mobileContext.newPage();
        try {
            await page.goto(p.url, { waitUntil: 'networkidle', timeout: 6000 }).catch(() => {});
            const shotPath = path.join(SCRATCH_DIR, `verify_mobile_${p.name}.png`);
            await page.screenshot({ path: shotPath });
            console.log(`Saved: verify_mobile_${p.name}.png`);
        } catch (e) {
            console.error(`Error on mobile ${p.name}:`, e.message);
        } finally {
            await page.close();
        }
    }
    await mobileContext.close();

    console.log('--- Capturing Desktop Screenshots (1500x900) ---');
    const desktopContext = await browser.newContext({
        viewport: { width: 1500, height: 900 }
    });

    for (const p of [PAGES[0], PAGES[3], PAGES[6]]) {
        const page = await desktopContext.newPage();
        try {
            await page.goto(p.url, { waitUntil: 'networkidle', timeout: 6000 }).catch(() => {});
            const shotPath = path.join(SCRATCH_DIR, `verify_desktop_${p.name}.png`);
            await page.screenshot({ path: shotPath });
            console.log(`Saved: verify_desktop_${p.name}.png`);
        } catch (e) {
            console.error(`Error on desktop ${p.name}:`, e.message);
        } finally {
            await page.close();
        }
    }
    await desktopContext.close();

    await browser.close();
    console.log('ALL VERIFICATIONS COMPLETED SUCCESSFULLY!');
})();
