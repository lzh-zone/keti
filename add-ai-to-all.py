#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量添加 AI 助手组件到所有 HTML 文件
"""

import os
import re
from pathlib import Path

# 要添加的 CSS 引用
CSS_LINK = '<link rel="stylesheet" href="css/ai-assistant.css">'

# 要添加的 JS 引用
JS_SCRIPT = '<script src="js/ai-assistant.js"></script>'

def add_ai_assistant_to_html(file_path):
    """向单个 HTML 文件添加 AI 助手组件引用"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经添加过
        if 'ai-assistant.css' in content and 'ai-assistant.js' in content:
            print(f'  ✓ 已存在: {file_path.name}')
            return False
        
        modified = False
        
        # 添加 CSS 引用 (在 </head> 之前)
        if 'ai-assistant.css' not in content:
            if '</head>' in content:
                content = content.replace('</head>', f'    {CSS_LINK}\n</head>')
                modified = True
        
        # 添加 JS 引用 (在 </body> 之前)
        if 'ai-assistant.js' not in content:
            if '</body>' in content:
                content = content.replace('</body>', f'{JS_SCRIPT}\n</body>')
                modified = True
            elif '</html>' in content:
                # 如果没有 </body>,在 </html> 之前添加
                content = content.replace('</html>', f'{JS_SCRIPT}\n</html>')
                modified = True
        
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'  ✓ 已添加: {file_path.name}')
            return True
        else:
            print(f'  - 跳过: {file_path.name}')
            return False
            
    except Exception as e:
        print(f'  ✗ 错误: {file_path.name} - {str(e)}')
        return False

def main():
    """主函数"""
    
    # 获取当前目录
    base_dir = Path('.')
    
    # 查找所有 HTML 文件
    html_files = list(base_dir.glob('*.html'))
    
    print(f'找到 {len(html_files)} 个 HTML 文件\n')
    print('开始添加 AI 助手组件...\n')
    
    success_count = 0
    skip_count = 0
    
    for html_file in sorted(html_files):
        if add_ai_assistant_to_html(html_file):
            success_count += 1
        else:
            skip_count += 1
    
    print(f'\n完成!')
    print(f'成功添加: {success_count} 个文件')
    print(f'已存在/跳过: {skip_count} 个文件')
    print(f'总计: {len(html_files)} 个文件')

if __name__ == '__main__':
    main()
