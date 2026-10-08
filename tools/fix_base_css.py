# -*- coding: utf-8 -*-
"""
浙江理工大学智能传感与驱动课题组网站
修复基础 CSS 中的固定高度与破坏性负边距
"""
import os

BASE_DIR = r"C:\Users\24415\Desktop\新建文件夹\keti\css"

# 1. 修复 4.academic_achievements.css
p4 = os.path.join(BASE_DIR, "4.academic_achievements.css")
with open(p4, "r", encoding="utf-8") as f:
    c4 = f.read()

c4 = c4.replace("height: 1108px;", "min-height: 400px; height: auto;")
c4 = c4.replace("height: 65px;", "min-height: 40px; height: auto;")
c4 = c4.replace("margin: -30px 0 -5px 0;", "margin: 10px 0 5px 0;")
c4 = c4.replace("margin: -50px 0 -5px 0;", "margin: 10px 0 5px 0;")
# 消除对所有 a 强行写死 height: 100px
c4 = c4.replace("height: 100px;", "min-height: 40px; height: auto;")

with open(p4, "w", encoding="utf-8") as f:
    f.write(c4)
print("Updated 4.academic_achievements.css")

# 2. 修复 3.team_intro.css
p3 = os.path.join(BASE_DIR, "3.team_intro.css")
with open(p3, "r", encoding="utf-8") as f:
    c3 = f.read()

c3 = c3.replace("height: 1064px;", "min-height: 400px; height: auto;")
c3 = c3.replace("height: 1200px;", "min-height: 500px; height: auto;")
c3 = c3.replace("height: 100px;", "min-height: 40px; height: auto;")

with open(p3, "w", encoding="utf-8") as f:
    f.write(c3)
print("Updated 3.team_intro.css")

# 3. 修复 2.news.css
p2 = os.path.join(BASE_DIR, "2.news.css")
with open(p2, "r", encoding="utf-8") as f:
    c2 = f.read()

c2 = c2.replace("height: 740px;", "min-height: 400px; height: auto;")
c2 = c2.replace("height: 992px;", "min-height: 400px; height: auto;")

with open(p2, "w", encoding="utf-8") as f:
    f.write(c2)
print("Updated 2.news.css")

# 4. 修复 6.recruit_student.css
p6 = os.path.join(BASE_DIR, "6.recruit_student.css")
with open(p6, "r", encoding="utf-8") as f:
    c6 = f.read()

c6 = c6.replace("height: 1250px;", "min-height: 400px; height: auto;")

with open(p6, "w", encoding="utf-8") as f:
    f.write(c6)
print("Updated 6.recruit_student.css")

print("All base CSS fixed successfully.")
