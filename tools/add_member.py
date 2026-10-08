#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
课题组团队成员快速录入工具 (Team Member Management Tool)
功能：
1. 录入新研究生（硕士生、博士生）或教师信息；
2. 自动生成标准规范的个人简介独立页面（如 3.3.team_intro_shuoshi_xxx.html）；
3. 自动在对应的汇总列表页面（如 3.3.team_intro_shuoshi.html）网格中追加成员照片和姓名卡片；
4. 保证个人主页的 Header、Nav、Tail 与全站高度一致。

用法示例：
  python tools/add_member.py
"""

import argparse
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def add_team_member(name: str, pinyin: str, category: str, photo: str, grade: str, direction: str, intro: str):
    """
    category: 'shuoshi' (硕士) 或 'boshi' (博士)
    """
    cat_cn = "硕士研究生" if category == "shuoshi" else "博士研究生"
    list_html_name = f"3.3.team_intro_shuoshi.html" if category == "shuoshi" else "3.2.team_intro_boshi.html"
    member_page_name = f"3.{3 if category == 'shuoshi' else 2}.team_intro_{category}_{pinyin}.html"

    list_page_path = BASE_DIR / list_html_name
    member_page_path = BASE_DIR / member_page_name

    photo_path = photo.strip() if photo.strip() else "images/pictures/default.jpg"

    # 1. 生成个人介绍独立页面
    member_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>浙江理工大学——刘爱萍教授课题组（{name}）</title>
    <link rel="icon" href="images/logo_24x24.ico" type="image/x-icon">
    <link rel="shortcut icon" href="images/logo_24x24.ico" type="image/x-icon">
    <link rel="stylesheet" href="css/3.team_intro.css">
    <link rel="stylesheet" href="css/ai-assistant.css">
</head>
<body>
    <div class="content">
        <div class="title">
            <img src="images/icon1.png" alt="">
            <a class="main" href="index.html">首页</a>
            <span>></span>
            <a href="3.team_intro.html">研究团队</a>
            <span>></span>
            <a href="{list_html_name}">{cat_cn}</a>
            <span>></span>
            <a href="{member_page_name}">{name}</a>
        </div>
        <div class="main_content">
            <div class="left" id="lef__">
                <ul>
                    <li class="team">研究团队</li>
                    <li><a href="3.1.team_intro_teachers.html">团队老师</a></li>
                    <li><a href="3.2.team_intro_boshi.html"{" class='selected'" if category == 'boshi' else ""}>博士研究生</a></li>
                    <li><a href="3.3.team_intro_shuoshi.html"{" class='selected'" if category == 'shuoshi' else ""}>硕士研究生</a></li>
                    <li><a href="3.4.team_intro_biye.html">已毕业学生</a></li>
                </ul>
            </div>
            <div class="right">
                <div class="top">
                    <h2>{name}</h2>
                </div>
                <div class="student" style="padding: 10px 0;">
                    <p><img src="{photo_path}" alt="{name}" style="height: 240px; border-radius: 6px;"></p>
                    <p style="margin-top: 20px;"><b>入学年级：</b>{grade}</p>
                    <p><b>研究方向：</b>{direction}</p>
                    <p><b>个人简介：</b>{intro}</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""
    with open(member_page_path, 'w', encoding='utf-8') as f:
        f.write(member_html)
    print(f"[OK] 成功生成个人主页: {member_page_name}")

    # 2. 在列表页面中追加头像和卡片
    if list_page_path.exists():
        with open(list_page_path, 'r', encoding='utf-8') as f:
            list_content = f.read()

        card_html = f"""
                    <a href="{member_page_name}">
                        <img src="{photo_path}" style="width: 140px; height: 186px; object-fit: cover;">
                        <p style="text-align: center; margin-top: 6px;">{name}</p>
                    </a>"""

        if '<div class="bottom grid_img">' in list_content:
            list_content = list_content.replace(
                '<div class="bottom grid_img">',
                f'<div class="bottom grid_img">{card_html}'
            )
            with open(list_page_path, 'w', encoding='utf-8') as f:
                f.write(list_content)
            print(f"[OK] 成功向 {list_html_name} 追加网格成员卡片")

    # 3. 运行全站同步工具保证 Header、Nav、Tail 一致
    from sync_site import main as run_sync
    run_sync()


def main():
    parser = argparse.ArgumentParser(description="团队成员快捷录入工具")
    parser.add_argument("--name", help="成员姓名 (如 宇航)")
    parser.add_argument("--pinyin", help="拼音或代号 (如 yuhang)")
    parser.add_argument("--category", choices=["shuoshi", "boshi"], default="shuoshi", help="成员类别 (shuoshi 或 boshi)")
    parser.add_argument("--photo", default="images/pictures/default.jpg", help="照片路径 (如 images/pictures/xxx.jpg)")
    parser.add_argument("--grade", default="2024级", help="入学年级")
    parser.add_argument("--direction", default="智能传感与驱动", help="研究方向")
    parser.add_argument("--intro", default="暂无详细简介。", help="个人简介或毕业院校")

    args, unknown = parser.parse_known_args()

    print("=" * 60)
    print("  浙江理工大学刘爱萍课题组 - 团队成员录入工具")
    print("=" * 60)

    name = args.name or input("请输入成员姓名 (如 宇航): ").strip()
    if not name:
        print("[CANCEL] 姓名不能为空。")
        return

    pinyin = args.pinyin or input("请输入拼音或英文字符代号 (如 yuhang): ").strip().lower()
    if not args.name:
        cat_input = input("成员类型 (1: 硕士研究生, 2: 博士研究生, 默认 1): ").strip()
        category = "boshi" if cat_input == "2" else "shuoshi"
        photo = input("照片路径 (如 images/pictures/xxx.jpg，留空使用默认图): ").strip() or "images/pictures/default.jpg"
        grade = input("入学年份 (如 2024级): ").strip() or "2024级"
        direction = input("研究方向 (如 智能水凝胶驱动器/柔性触觉传感): ").strip() or "智能传感与驱动"
        intro = input("个人简介或本科毕业院校: ").strip() or "暂无详细简介。"
    else:
        category = args.category
        photo = args.photo
        grade = args.grade
        direction = args.direction
        intro = args.intro

    add_team_member(name, pinyin, category, photo, grade, direction, intro)


if __name__ == '__main__':
    main()
