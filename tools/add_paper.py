#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
课题组学术论文便捷添加与年份扩展工具 (Paper Management Tool)
功能：
1. 向指定年份的论文列表（如 4.1.2026.html）中添加新论文条目；
2. 自动加粗通讯作者/课题组负责人（Aiping Liu 等）；
3. 自动维护条目序号与排版格式；
4. 若年份页面不存在（如新年份 2027 年），自动创建新页面并自动更新全站导航和侧边栏。

用法示例：
  # 交互式引导添加：
  python tools/add_paper.py

  # 命令行快捷添加：
  python tools/add_paper.py --year 2026 --title "Paper Title" --authors "Hang Yu, Aiping Liu" --journal "Chemical Engineering Journal, 2026, 541: 177786" --doi "10.1016/j.cej.2026.177786" --pdf "static/2026/paper.pdf"
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def format_authors(authors: str) -> str:
    """自动高亮课题组负责人与主要作者"""
    authors = re.sub(r'\bAiping Liu\b', '<b>Aiping Liu</b>', authors, flags=re.I)
    authors = re.sub(r'刘爱萍', '<b>刘爱萍</b>', authors)
    return authors


def generate_paper_html(index: int, title: str, authors: str, journal: str, doi: str, pdf_path: str, is_first: bool = False) -> str:
    """生成单条论文的 HTML 代码"""
    doi_clean = doi.strip()
    doi_url = doi_clean if doi_clean.startswith('http') else f'https://doi.org/{doi_clean}'
    top_class = " toplunwen" if is_first else ""

    return f"""
					<a class="lunwenStyle{top_class}" href="{pdf_path}" target="_blank">({index}) {title}</a>
                    <div>{authors}</div>
                    <div class="journal"><i>{journal}</i></div>
                    <a href="{doi_url}" class="DOI" target="_blank" style="border-bottom: 2px dashed #eee;padding-bottom: 28px;">DOI: {doi_clean}</a>
"""


def create_new_year_page(year: str) -> Path:
    """如果该年份不存在，自动基于最近一年创建新年份页面并更新全站引用"""
    new_html = BASE_DIR / f"4.1.{year}.html"
    if new_html.exists():
        return new_html

    # 寻找已有最新年份页面作为模板
    existing_years = []
    for f in BASE_DIR.glob("4.1.20*.html"):
        match = re.search(r'4\.1\.(\d{4})\.html', f.name)
        if match:
            existing_years.append(int(match.group(1)))

    latest_year = str(max(existing_years)) if existing_years else "2026"
    latest_html = BASE_DIR / f"4.1.{latest_year}.html"

    print(f"正在基于 {latest_html.name} 创建新年份页面: {new_html.name} ...")
    shutil.copy(latest_html, new_html)

    with open(new_html, 'r', encoding='utf-8') as f:
        content = f.read()

    # 替换面包屑、标题与年份数字
    content = content.replace(f'<h2>{latest_year}</h2>', f'<h2>{year}</h2>')
    content = content.replace(f'>{latest_year}<', f'>{year}<')
    content = content.replace(f'4.1.{latest_year}.html', f'4.1.{year}.html')

    # 清空内容区域准备插入新论文
    content = re.sub(
        r'(<div class="bottom">)(.*?)(</div>\s*<div class="change_page">)',
        r'\1\n                    <!-- 论文列表 -->\n                \3',
        content,
        flags=re.DOTALL
    )

    with open(new_html, 'w', encoding='utf-8') as f:
        f.write(content)

    # 在 common/nav.html 中更新最新年份
    nav_file = BASE_DIR / "common" / "nav.html"
    if nav_file.exists():
        with open(nav_file, 'r', encoding='utf-8') as f:
            nav_content = f.read()
        nav_content = nav_content.replace(f'4.1.{latest_year}.html', f'4.1.{year}.html')
        with open(nav_file, 'w', encoding='utf-8') as f:
            nav_content = f.write(nav_content)

    # 同步更新侧边栏，将新年份插入到各个成果页面的侧边栏最前
    sidebar_old = f'<li class="achievements_son"><a href="4.1.{latest_year}.html"'
    sidebar_new = f'<li class="achievements_son"><a href="4.1.{year}.html">{year}</a></li>\n                    <li class="achievements_son"><a href="4.1.{latest_year}.html"'

    for fpath in BASE_DIR.glob("4.*.html"):
        with open(fpath, 'r', encoding='utf-8') as f:
            fc = f.read()
        if f'4.1.{year}.html' not in fc:
            fc = fc.replace(sidebar_old, sidebar_new)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(fc)

    print(f"新年份 {year} 页面及全站导航引用注册成功！")
    return new_html


def add_paper(year: str, title: str, authors: str, journal: str, doi: str, pdf_path: str):
    """向对应年份页面插入新论文"""
    page_path = BASE_DIR / f"4.1.{year}.html"
    if not page_path.exists():
        page_path = create_new_year_page(year)

    with open(page_path, 'r', encoding='utf-8') as f:
        content = f.read()

    formatted_authors = format_authors(authors)

    # 统计已有论文条目以计算新论文序号
    existing_papers = re.findall(r'<a class="lunwenStyle[^>]*>\s*\(\d+\)', content)
    new_index = len(existing_papers) + 1

    paper_chunk = generate_paper_html(
        index=new_index,
        title=title,
        authors=formatted_authors,
        journal=journal,
        doi=doi,
        pdf_path=pdf_path,
        is_first=(new_index == 1)
    )

    # 插入到 <div class="bottom"> 内部末尾
    if '<div class="bottom">' in content:
        # 在 bottom 闭合之前插入
        bottom_pattern = r'(<div class="bottom">[\s\S]*?)(</div>\s*<div class="change_page">)'
        if re.search(bottom_pattern, content):
            new_content = re.sub(bottom_pattern, rf'\1{paper_chunk}\n                \2', content, count=1)
            with open(page_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"[OK] 成功向 {page_path.name} 添加论文 ({new_index}): {title}")
            return True

    print(f"[ERROR] 未能在 {page_path.name} 中找到目标插入位置 <div class='bottom'>")
    return False


def main():
    parser = argparse.ArgumentParser(description="学术论文快捷录入工具")
    parser.add_argument("--year", help="发表年份 (例如 2026)")
    parser.add_argument("--title", help="论文题目")
    parser.add_argument("--authors", help="作者列表 (英文逗号分隔)")
    parser.add_argument("--journal", help="期刊名称、年份、卷期页码")
    parser.add_argument("--doi", help="DOI 编号或完整链接")
    parser.add_argument("--pdf", default="#", help="PDF 文件相对路径 (如 static/2026/xxx.pdf，无则填 #)")

    args = parser.parse_args()

    print("=" * 60)
    print("  浙江理工大学刘爱萍课题组 - 论文录入与管理工具")
    print("=" * 60)

    # 若未提供完整命令行参数，启动交互式输入
    year = args.year or input("请输入论文年份 (默认 2026): ").strip() or "2026"
    title = args.title or input("请输入论文题目: ").strip()
    authors = args.authors or input("请输入作者列表 (英文逗号分隔): ").strip()
    journal = args.journal or input("请输入期刊及卷期信息 (如 Chemical Engineering Journal, 2026, 541: 177786): ").strip()
    doi = args.doi or input("请输入 DOI (如 10.1016/j.cej.2026.177786): ").strip()
    pdf = args.pdf or input("请输入 PDF 相对路径 (默认 #): ").strip() or "#"

    if not title:
        print("[CANCEL] 论文题目不能为空，已退出。")
        return

    add_paper(year, title, authors, journal, doi, pdf)

    # 询问是否执行全站同步
    print("\n是否运行全站组件同步以确保各页面侧边栏和导航保持最新？(Y/n): ", end="")
    choice = input().strip().lower()
    if choice in ('', 'y', 'yes'):
        from sync_site import main as run_sync
        run_sync()


if __name__ == '__main__':
    main()
