import glob
import re

for filepath in glob.glob('css/*.css'):
    if 'responsive.css' in filepath or 'ai-assistant.css' in filepath:
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace hardcoded widths
    content = re.sub(r'width:\s*1500px;', 'width: 100%; max-width: 1500px;', content)
    content = re.sub(r'min-width:\s*1200px;', 'min-width: 0;', content)
    
    # Replace hardcoded heights
    content = re.sub(r'height:\s*1160px;', 'height: auto;', content)
    content = re.sub(r'height:\s*1000px;', 'height: auto;', content)
    
    # Fix the percentage margins for desktop header text in 1.index.css
    content = content.replace('margin: 3% 0px 0 17%;', 'margin: 45px 0px 0 255px;')
    content = content.replace('margin: 4% 11% 0 0;', 'margin: 48px 165px 0 0;')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Patched {filepath}")
