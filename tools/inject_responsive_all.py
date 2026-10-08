# -*- coding: utf-8 -*-
"""
浙江理工大学智能传感与驱动课题组网站
全站 HTML 统一注入 responsive.css 工具
"""
import os
import glob

SITE_DIR = r"C:\Users\24415\Desktop\新建文件夹\keti"

def inject_responsive():
    html_files = glob.glob(os.path.join(SITE_DIR, "*.html"))
    modified_count = 0
    already_count = 0

    css_tag = '    <link rel="stylesheet" href="css/responsive.css">\n'

    for file_path in html_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if "responsive.css" in content:
            already_count += 1
            continue

        if "</head>" in content:
            new_content = content.replace("</head>", css_tag + "</head>", 1)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            modified_count += 1
            print(f"注入成功: {os.path.basename(file_path)}")
        else:
            print(f"警告: 未找到 </head> 标签: {os.path.basename(file_path)}")

    print(f"\n注入完成: 新增 {modified_count} 个文件, 已包含 {already_count} 个文件。")

if __name__ == "__main__":
    inject_responsive()
