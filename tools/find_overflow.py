# -*- coding: utf-8 -*-
import subprocess

html_content = open('4.1.2026.html', 'r', encoding='utf-8').read()

# Add script at end of body
injection = """
<script>
window.addEventListener('load', () => {
    let res = [];
    document.querySelectorAll('*').forEach(el => {
        let b = el.getBoundingClientRect();
        if (b.width > 375 || b.right > 375) {
            res.push({
                tag: el.tagName,
                cls: el.className,
                w: Math.round(b.width),
                l: Math.round(b.left),
                r: Math.round(b.right)
            });
        }
    });
    fetch('http://localhost:8000/report_overflow', {
        method: 'POST',
        body: JSON.stringify(res)
    }).catch(e => {});
});
</script>
"""
