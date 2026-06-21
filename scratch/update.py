import os
import glob
import shutil
import re

# 1. Create 4.1.2026.html from 4.1.2025.html
shutil.copy('4.1.2025.html', '4.1.2026.html')

with open('4.1.2026.html', 'r', encoding='utf-8') as f:
    content2026 = f.read()

# Replace the breadcrumb year
content2026 = content2026.replace('<a href="4.1.2025.html">2025</a>', '<a href="4.1.2026.html">2026</a>')

# Replace the h2 title
content2026 = content2026.replace('<h2>2025</h2>', '<h2>2026</h2>')

# New papers HTML
papers_html = """
					<a class="lunwenStyle toplunwen" href="static/2026/1-s2.0-S1385894726052472-main.pdf" target="_blank">(1) Bionic Tursiops Truncatus-inspired dual-mode sensor for proximity sensing and high-resolution tactile perception</a>
                    <div>Hang Yu, Zhao Xu, Haowen Chen, Guangchao Wang, Qiang Sun, Haoran Fu, Huaping Wu, <b>Aiping Liu</b></div>
                    <div class="journal"><i>Chemical Engineering Journal</i>, 2026, 541: 177786.</div>
                    <a href="https://doi.org/10.1016/j.cej.2026.177786" class="DOI" target="_blank" style="border-bottom: 2px dashed #eee;padding-bottom: 28px;">DOI: 10.1016/j.cej.2026.177786</a>

					<a class="lunwenStyle" href="static/2026/shape-memory-conductive-hydrogels-featuring-permanent-and-temporary-dual-state-programmability.pdf" target="_blank">(2) Shape-Memory Conductive Hydrogels Featuring Permanent and Temporary Dual-State Programmability</a>
                    <div>Ping Guo, Jie Zhou, Chengnan Qian, Wenjie Cao, Yang Yu, Lin Cheng, Daoyou Guo, Huaping Wu, <b>Aiping Liu</b></div>
                    <div class="journal"><i>ACS Applied Polymer Materials</i>, 2025, 7, 15659-15670.</div>
                    <a href="https://doi.org/10.1021/acsapm.5c03453" class="DOI" target="_blank" style="border-bottom: 2px dashed #eee;padding-bottom: 28px;">DOI: 10.1021/acsapm.5c03453</a>
"""

# Replace the bottom div content
# Find everything between <div class="bottom"> and </div>\n                <div class="change_page">
import re
content2026 = re.sub(
    r'(<div class="bottom">)(.*?)(</div>\s*<div class="change_page">)', 
    rf'\1\n{papers_html}\n                \3', 
    content2026, 
    flags=re.DOTALL
)

# Update sidebar in 4.1.2026.html
# Add 2026
content2026 = content2026.replace(
    '<li class="achievements_son"><a href="4.1.2025.html" class="selected">2025</a></li>',
    '<li class="achievements_son"><a href="4.1.2026.html" class="selected">2026</a></li>\n                    <li class="achievements_son"><a href="4.1.2025.html">2025</a></li>'
)

# In the bottom change_page, no need to change much, just leave it or set selected to 2026 if it exists.
# We'll replace '<li class="six selected"><a href="4.1.2024.html">1</a></li>' -> we don't need change_page if only 2 papers. Wait, the change_page says 2024, let's just replace the link with 2026.
content2026 = content2026.replace(
    '<li class="six selected"><a href="4.1.2024.html">1</a></li>',
    '<li class="six selected"><a href="4.1.2026.html">1</a></li>'
)

with open('4.1.2026.html', 'w', encoding='utf-8') as f:
    f.write(content2026)


# 2. Update all other HTML files
html_files = glob.glob('*.html')

for f in html_files:
    if f == '4.1.2026.html':
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    original_content = content
    
    # 2.1 Update Nav Bar and main link
    content = content.replace('<li><a href="4.1.2025.html">论文</a></li>', '<li><a href="4.1.2026.html">论文</a></li>')
    content = content.replace('<li><a href="4.1.2025.html" class="selected">论文</a></li>', '<li><a href="4.1.2026.html" class="selected">论文</a></li>')
    
    # 2.2 Insert 2026 into sidebar
    if '<li class="achievements_son"><a href="4.1.2026.html"' not in content:
        content = content.replace(
            '<li class="achievements_son"><a href="4.1.2025.html" class="selected">2025</a></li>',
            '<li class="achievements_son"><a href="4.1.2026.html">2026</a></li>\n                    <li class="achievements_son"><a href="4.1.2025.html" class="selected">2025</a></li>'
        )
        content = content.replace(
            '<li class="achievements_son"><a href="4.1.2025.html">2025</a></li>',
            '<li class="achievements_son"><a href="4.1.2026.html">2026</a></li>\n                    <li class="achievements_son"><a href="4.1.2025.html">2025</a></li>'
        )
        
    if original_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)

print("Done updating HTMLs.")
