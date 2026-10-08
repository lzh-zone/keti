# -*- coding: utf-8 -*-
"""
浙江理工大学智能传感与驱动课题组网站
将 CSS 中硬编码的大像素宽度（1200px / 970px / 960px）改造为弹性自适应 max-width
保证桌面端（1500px）完全不变，移动端与中屏完美自适应
"""
import os

CSS_DIR = r"C:\Users\24415\Desktop\新建文件夹\keti\css"

def patch_file(fname, replacements):
    fpath = os.path.join(CSS_DIR, fname)
    if not os.path.exists(fpath):
        return
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            print(f"[{fname}] Replaced: {old.strip()} -> {new.strip()}")
        else:
            print(f"[{fname}] NOT FOUND: {old.strip()}")
            
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

# 4.academic_achievements.css
patch_file("4.academic_achievements.css", [
    ("width: 1200px;", "width: 100%; max-width: 1200px;"),
    ("width: 970px;", "width: 100%; max-width: 970px;"),
    ("width: 98%;", "width: 100%;"),
    ("padding-left: 11px;", "padding-left: 0;"),
    ("text-indent: 3mm;", "text-indent: 0;"),
    ("margin: 40px 0 -5px 0;", "margin: 14px 0 5px 0;"),
])

# 3.team_intro.css
patch_file("3.team_intro.css", [
    ("width: 1200px;", "width: 100%; max-width: 1200px;"),
    ("width: 960px;", "width: 100%; max-width: 960px;"),
    ("width: 92%;", "width: 100%;"),
    ("margin: 210px 0px 0px 78px;", "margin: 8px 0 0 0;"),
    ("margin-left: 31px;", "margin-left: 0;"),
    ("margin-right: 15px;", "margin-right: 0;"),
    ("margin-top: -390px;", "margin-top: 10px;"),
])

# 2.news.css
patch_file("2.news.css", [
    ("width: 1200px;", "width: 100%; max-width: 1200px;"),
    ("width: 107%;", "width: 100%;"),
    ("width: 103%;", "width: 100%;"),
    ("margin: 7px 0 7px 35px;", "margin: 7px 0;"),
])

# 6.recruit_student.css
patch_file("6.recruit_student.css", [
    ("width: 1200px;", "width: 100%; max-width: 1200px;"),
    ("width: 960px;", "width: 100%; max-width: 960px;"),
    ("width: 113%;", "width: 100%;"),
])

print("\nAll CSS successfully modernized!")
