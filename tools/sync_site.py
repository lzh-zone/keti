#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
课题组网站全站组件一键同步维护工具 (Site Component Synchronizer)
功能：
1. 统一管理公共组件（common/header.html, common/nav.html, common/tail.html）；
2. 一键批量同步更新全站所有 HTML 页面的头部、导航栏和页脚；
3. 智能根据当前页面定位并激活当前导航栏项的选中状态 (class="selected")；
4. 确保每个页面具备移动端 Viewport 和必要的基础 Meta/样式/脚本引用。

用法：
  python tools/sync_site.py          # 执行同步更新
  python tools/sync_site.py --check  # 仅检查差异，不写入文件
"""

import os
import re
import sys
from pathlib import Path

# 项目根目录 (当前 tools 目录的上一级)
BASE_DIR = Path(__file__).resolve().parent.parent

COMMON_DIR = BASE_DIR / "common"
HEADER_TEMPLATE_PATH = COMMON_DIR / "header.html"
NAV_TEMPLATE_PATH = COMMON_DIR / "nav.html"
TAIL_TEMPLATE_PATH = COMMON_DIR / "tail.html"


def get_nav_with_active_state(nav_template: str, filename: str) -> str:
    """根据当前文件名智能设置导航栏高亮 class='selected'"""
    content = nav_template

    target_id = None
    if filename == "index.html":
        target_id = "nav-item-home"
    elif filename.startswith("2."):
        target_id = "nav-item-news"
    elif filename.startswith("3."):
        target_id = "nav-item-team"
    elif filename.startswith("4."):
        target_id = "nav-item-achieve"
    elif filename.startswith("5."):
        target_id = "nav-item-resource"
    elif filename.startswith("6."):
        target_id = "nav-item-recruit"

    if target_id:
        # 在指定 id 的 a 标签上添加 class="selected"
        content = re.sub(
            rf'(<a\s+[^>]*id="{target_id}"[^>]*)>',
            r'\1 class="selected">',
            content,
            flags=re.IGNORECASE,
        )

    return content


def sync_html_file(file_path: Path, header_tpl: str, nav_tpl: str, tail_tpl: str, check_only: bool = False) -> bool:
    """同步单个 HTML 文件的 Header, Nav, Tail 与 Meta"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            html = f.read()
    except Exception as e:
        print(f"  [ERROR] 读取失败: {file_path.name} ({e})")
        return False

    original_html = html

    # 1. 确保 Viewport Meta 存在 (移动端适配)
    if not re.search(r'<meta\s+name=["\']viewport["\']', html, re.I):
        if "<head>" in html:
            html = re.sub(
                r"<head>",
                '<head>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
                html,
                count=1,
                flags=re.I,
            )

    # 2. 确保 AI 助手组件引用存在
    if "ai-assistant.css" not in html and "</head>" in html:
        html = html.replace("</head>", '    <link rel="stylesheet" href="css/ai-assistant.css">\n</head>')
    if "ai-assistant.js" not in html and "</body>" in html:
        html = html.replace("</body>", '    <script src="js/ai-assistant.js"></script>\n</body>')

    # 3. 替换 Header 区域
    # 匹配从 <!-- 1、header部分 --> 或 <div class="header"> 开始，直到 <div class="nav" 之前
    header_regex = re.compile(
        r"(<!--\s*1[、\.,]?\s*header[^\>]*-->\s*)?<div\s+class=[\"']header[\"']>.*?</div>\s*</div>(?=\s*(?:<!--\s*2|<div\s+class=[\"']nav[\"']))",
        re.DOTALL | re.IGNORECASE,
    )
    if header_regex.search(html):
        html = header_regex.sub(header_tpl.strip(), html, count=1)

    # 4. 替换 Nav 区域 (注意：nav 内部没有嵌套 div，首个 </div> 即为闭合标签，绝不向后多吞任何标签)
    active_nav = get_nav_with_active_state(nav_tpl, file_path.name)
    nav_regex = re.compile(
        r"(?:<!--\s*2[、\.,]?\s*导航[^\>]*-->\s*)?<div\s+class=[\"']nav[\"'][^>]*>(?:(?!</div>)[\s\S])*?</div>",
        re.IGNORECASE,
    )
    if nav_regex.search(html):
        html = nav_regex.sub(active_nav.strip(), html, count=1)

    # 5. 替换 Tail 区域
    tail_regex = re.compile(
        r"(<!--\s*5[、\.,]?\s*尾部[^\>]*-->\s*)?<div\s+class=[\"']tail[\"']>.*?</div>\s*</div>(?=\s*(?:<script|</body>|$))",
        re.DOTALL | re.IGNORECASE,
    )
    if tail_regex.search(html):
        html = tail_regex.sub(tail_tpl.strip(), html, count=1)

    # 6. 统一修正可能存在的 1.index.html 死链
    html = re.sub(r'href=["\']1\.index\.html["\']', 'href="index.html"', html)

    # 检查是否修改
    if html != original_html:
        if not check_only:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"  [OK] 已同步: {file_path.name}")
        else:
            print(f"  [DIFF] 需要更新: {file_path.name}")
        return True
    else:
        return False


def main():
    check_only = "--check" in sys.argv

    print("=" * 60)
    print("  浙江理工大学刘爱萍课题组 - 网站全站组件智能同步工具")
    print("=" * 60)

    # 检查模板文件
    for tpl_path in [HEADER_TEMPLATE_PATH, NAV_TEMPLATE_PATH, TAIL_TEMPLATE_PATH]:
        if not tpl_path.exists():
            print(f"[FATAL] 未找到模板文件: {tpl_path}")
            sys.exit(1)

    with open(HEADER_TEMPLATE_PATH, "r", encoding="utf-8") as f:
        header_tpl = f.read()
    with open(NAV_TEMPLATE_PATH, "r", encoding="utf-8") as f:
        nav_tpl = f.read()
    with open(TAIL_TEMPLATE_PATH, "r", encoding="utf-8") as f:
        tail_tpl = f.read()

    # 扫描根目录下所有 HTML
    html_files = sorted(
        [f for f in BASE_DIR.glob("*.html") if f.is_file()],
        key=lambda x: x.name,
    )

    print(f"共发现 {len(html_files)} 个主站 HTML 页面。开始同步...\n")

    changed_count = 0
    for file_path in html_files:
        if sync_html_file(file_path, header_tpl, nav_tpl, tail_tpl, check_only=check_only):
            changed_count += 1

    print("\n" + "=" * 60)
    if check_only:
        print(f"检查完毕！共有 {changed_count} / {len(html_files)} 个文件需要同步。")
    else:
        print(f"同步完毕！共更新了 {changed_count} / {len(html_files)} 个文件。全站组件已保持高度统一！")
    print("=" * 60)


if __name__ == "__main__":
    main()
