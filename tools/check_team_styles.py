import glob, re

for f in sorted(glob.glob('3*.html')):
    c = open(f, encoding='utf-8', errors='ignore').read()
    m_top = re.findall(r'margin-top:\s*\d+px', c)
    h_style = re.findall(r'style="[^"]*height:\s*\d+px[^"]*"', c)
    if m_top or h_style:
        print(f"{f:35} -> m_top: {m_top} | h_style: {h_style}")
