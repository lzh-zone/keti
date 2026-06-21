import glob
import re

for filename in glob.glob('*.html'):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove existing viewport meta to prevent duplicates
    html = re.sub(r'<meta\s+name=["\']viewport["\'][^>]*>', '', html, flags=re.IGNORECASE)
    
    # Also remove existing responsive.css link if present
    html = re.sub(r'<link\s+rel=["\']stylesheet["\']\s+href=["\']css/responsive.css["\']\s*/*>', '', html, flags=re.IGNORECASE)

    # Inject viewport and responsive.css right before </head>
    injection = '''
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/responsive.css">
</head>'''
    
    html = re.sub(r'</head>', injection, html, flags=re.IGNORECASE)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Processed {filename}")
