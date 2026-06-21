import re

for f in ['index.html', '2.life.html']:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = re.sub(r'<meta\s+name=["\']viewport["\'][^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<link\s+rel=["\']stylesheet["\']\s+href=["\']css/responsive.css["\'][^>]*>', '', content, flags=re.IGNORECASE)
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
