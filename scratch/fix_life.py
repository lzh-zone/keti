import re
with open('2.life.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'\{\s*src:\s*\'([^\']+)\'\s*\}', r'"\1"', html)

with open('2.life.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed strings in 2.life.html")
