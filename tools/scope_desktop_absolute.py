# -*- coding: utf-8 -*-
"""
浙江理工大学智能传感与驱动课题组网站
将桌面端专用的 absolute 定位与 left: 240px 安全包裹到 @media (min-width: 993px) 内部
彻底根治移动端右侧内容被推到 240px 外的致命 Bug
"""
import os, re

CSS_DIR = r"C:\Users\24415\Desktop\新建文件夹\keti\css"

files = [
    "4.academic_achievements.css",
    "3.team_intro.css",
    "2.news.css",
    "6.recruit_student.css"
]

for fname in files:
    fpath = os.path.join(CSS_DIR, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()

    # 匹配 .content .title { position: absolute; ... }
    # 替换 position: absolute 为桌面端专用或保留默认
    # 最核心的是：
    # 1. 把 .content .main_content { position: absolute; width: 79%; z-index: 0; }
    # 2. 把 .content .main_content .right { position: absolute; ... left: 240px; ... }
    
    # 改造方法：
    # 在样式表中找到 .content .main_content { ... } 和 .content .main_content .right { ... }
    # 将其替换为包裹在 @media screen and (min-width: 993px) 中
    
    def repl_main(match):
        block = match.group(0)
        return f"@media screen and (min-width: 993px) {{\n{block}\n}}"

    # 针对 .content .title
    pattern_title = r"(\.content\s+\.title\s*\{[^}]*position\s*:\s*absolute[^}]*\})"
    c = re.sub(pattern_title, repl_main, c, flags=re.MULTILINE)

    # 针对 .content .main_content { position: absolute; ... }
    pattern_main = r"(\.content\s+\.main_content\s*\{[^}]*position\s*:\s*absolute[^}]*\})"
    c = re.sub(pattern_main, repl_main, c, flags=re.MULTILINE)

    # 针对 .content .main_content .right { position: absolute; ... left:\s*240px[^}]*\})"
    pattern_right = r"(\.content\s+\.main_content\s+\.right\s*\{[^}]*left\s*:\s*240px[^}]*\})"
    c = re.sub(pattern_right, repl_main, c, flags=re.MULTILINE)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(c)
    print(f"Successfully processed {fname}")

print("\nAll CSS absolute positions successfully scoped to desktop!")
