import glob
import re

for f in glob.glob('css/*.css'):
    if f == 'css\\responsive.css':
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = re.sub(r'width:\s*1500px;', 'width: 100%; max-width: 1500px;', content)
    content = re.sub(r'min-width:\s*1200px;', 'min-width: 0;', content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Patched {f}")
