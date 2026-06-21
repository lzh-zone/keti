import glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content.replace('<li><a href="4.1.2025.html" class="selected">论文</a></li>', '<li><a href="4.1.2026.html" class="selected">论文</a></li>')
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
