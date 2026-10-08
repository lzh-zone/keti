import re

c = open('index.html', encoding='utf-8').read()
matches = re.findall(r'<div class="all_title">[\s\S]*?</div>\s*</div>', c)
for i, m in enumerate(matches):
    print(f"=== TITLE {i+1} ===")
    print(m)
