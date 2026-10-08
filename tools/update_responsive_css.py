# -*- coding: utf-8 -*-
"""
浙江理工大学智能传感与驱动课题组网站
终极响应式适配规则构建脚本 (responsive.css)
"""

CSS_PATH = r"C:\Users\24415\Desktop\新建文件夹\keti\css\responsive.css"

with open(CSS_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 截取 1200px 之前的基础桌面样式
split_token = "@media screen and (max-width: 992px)"
pos = content.find(split_token)
if pos == -1:
    pos = content.find("平板与移动端通用核心重构")
    pos = content.rfind("/* =", 0, pos)

part1 = content[:pos]

new_responsive = part1 + """/* ==========================================================================
   平板与移动端通用核心重构 (<= 992px)
   ========================================================================== */
@media screen and (max-width: 992px) {
    /* 1. 根容器彻底防止横向滚动与溢出 */
    html, body {
        width: 100% !important;
        max-width: 100% !important;
        overflow-x: hidden !important;
    }

    body {
        min-width: 0 !important;
        height: auto !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* 限制 content 内部所有元素绝不超出父容器 */
    .content, .content * {
        max-width: 100% !important;
        box-sizing: border-box !important;
    }

    /* 2. 彻底解除二级页面的写死绝对定位与尺寸 */
    .content {
        position: static !important;
        top: auto !important;
        left: auto !important;
        width: 95% !important;
        height: auto !important;
        min-height: auto !important;
        margin: 15px auto 40px auto !important;
        padding: 0 !important;
    }

    .content .title {
        position: static !important;
        top: auto !important;
        left: auto !important;
        width: 100% !important;
        height: auto !important;
        line-height: 1.5 !important;
        margin-bottom: 15px !important;
        padding: 8px 4px !important;
        display: flex !important;
        align-items: center !important;
        flex-wrap: wrap !important;
        gap: 6px !important;
        border-bottom: 1px solid #e5e7eb !important;
    }

    .content .title img {
        position: static !important;
        margin: 0 !important;
        vertical-align: middle !important;
    }

    .content .title .main {
        margin-left: 4px !important;
    }

    .content .main_content {
        position: static !important;
        top: auto !important;
        left: auto !important;
        width: 100% !important;
        height: auto !important;
        display: flex !important;
        flex-direction: column !important;
        gap: 15px !important;
    }

    /* 侧边栏转为顶部横向标签卡片 */
    .content .main_content .left {
        position: static !important;
        top: auto !important;
        left: auto !important;
        width: 100% !important;
        min-width: 100% !important;
        height: auto !important;
        margin: 0 0 15px 0 !important;
        padding: 12px 14px !important;
        background: #fff !important;
        border-radius: 8px !important;
        box-shadow: 0 1px 4px rgba(0,0,0,0.06) !important;
    }

    .content .main_content .left ul {
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 6px !important;
        padding: 0 !important;
        margin: 0 !important;
        width: 100% !important;
    }

    .content .main_content .left li {
        width: auto !important;
        height: auto !important;
        margin: 0 !important;
        line-height: normal !important;
    }

    .content .main_content .left li a {
        padding: 6px 12px !important;
        font-size: 13px !important;
        border-radius: 4px !important;
        background-color: #f3f4f6 !important;
        color: #4b5563 !important;
        display: inline-block !important;
        transition: all 0.2s ease !important;
    }

    .content .main_content .left li a.selected,
    .content .main_content .left li .selected {
        background-color: #2f72c0 !important;
        color: #ffffff !important;
    }

    .content .main_content .left .achievements,
    .content .main_content .left .team,
    .content .main_content .left .recruit {
        width: 100% !important;
        margin: 0 0 8px 0 !important;
        height: auto !important;
        line-height: normal !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        color: #1f2937 !important;
        border-bottom: 2px solid #2f72c0 !important;
        padding-bottom: 6px !important;
        background: transparent !important;
    }

    /* 正文内容卡片解除定位与固定高度 */
    .content .main_content .right {
        position: static !important;
        top: auto !important;
        left: auto !important;
        width: 100% !important;
        min-width: 0 !important;
        height: auto !important;
        border-left: none !important;
        padding: 16px !important;
        background: #fff !important;
        border-radius: 8px !important;
        box-shadow: 0 1px 4px rgba(0,0,0,0.06) !important;
    }

    .content .main_content .right .top,
    .content .main_content .right .topzhuanli {
        width: 100% !important;
        height: auto !important;
        line-height: normal !important;
        text-align: left !important;
        margin-bottom: 14px !important;
        padding-bottom: 8px !important;
        border-left: none !important;
        border-bottom: 1px solid #e5e7eb !important;
    }

    .content .main_content .right .bottom,
    .content .main_content .right .bottomjijin {
        width: 100% !important;
        height: auto !important;
        min-height: 0 !important;
        border-left: none !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    .content .main_content .right .bottom .lunwenStyle,
    .content .main_content .right .bottom a,
    .content .main_content .right .bottomjijin a {
        display: block !important;
        width: 100% !important;
        height: auto !important;
        min-height: 0 !important;
        font-size: 14px !important;
        line-height: 1.5 !important;
        margin: 14px 0 6px 0 !important;
        padding: 0 !important;
        border: none !important;
        text-indent: 0 !important;
        word-break: normal !important;
        overflow-wrap: break-word !important;
        white-space: normal !important;
    }

    .content .main_content .right .bottom div,
    .content .main_content .right .bottom .journal,
    .content .main_content .right .bottom .DOI {
        padding: 0 !important;
        margin: 4px 0 !important;
        width: 100% !important;
        font-size: 13px !important;
        line-height: 1.5 !important;
        word-break: normal !important;
        overflow-wrap: break-word !important;
    }

    .content .main_content .right .bottom .DOI {
        display: block !important;
        width: 100% !important;
        height: auto !important;
        word-break: break-all !important;
        padding-bottom: 12px !important;
    }

    /* 师生主页排版 */
    .content .main_content .right .student,
    .student, .content .pic {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
        height: auto !important;
        text-align: center !important;
    }

    .content .main_content .right .student img,
    .student p img, .student img {
        position: static !important;
        display: block !important;
        height: auto !important;
        max-height: 240px !important;
        width: auto !important;
        max-width: 70% !important;
        border-radius: 8px !important;
        margin: 10px auto !important;
    }

    .content .main_content .right .student p,
    .student p {
        width: 100% !important;
        margin: 12px 0 !important;
        padding: 0 !important;
        line-height: 1.8 !important;
        text-indent: 2em !important;
        text-align: justify !important;
        word-break: break-word !important;
    }

    /* 成员网格列表 (平板3列) */
    .content .main_content .right .grid_img,
    .content .main_content .right .bottom.grid_img,
    .grid_img {
        display: grid !important;
        grid-template-columns: repeat(3, 1fr) !important;
        gap: 16px !important;
        width: 100% !important;
        height: auto !important;
        min-height: 0 !important;
        margin: 10px 0 !important;
        padding: 0 !important;
    }

    .content .main_content .right .grid_img a,
    .content .main_content .right .bottom.grid_img a,
    .grid_img a {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: flex-start !important;
        width: 100% !important;
        height: auto !important;
        min-height: 0 !important;
        margin: 0 !important;
        margin-top: 0 !important;
        padding: 10px 6px !important;
        background: #f8fafc !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
        text-decoration: none !important;
    }

    .content .main_content .right .grid_img a img,
    .content .main_content .right .grid_img img,
    .content .main_content .right .bottom.grid_img img,
    .grid_img a img {
        position: static !important;
        display: block !important;
        width: 120px !important;
        height: 155px !important;
        max-width: 90% !important;
        object-fit: cover !important;
        border-radius: 6px !important;
        margin: 0 auto !important;
        padding: 0 !important;
    }

    .content .main_content .right .grid_img a p,
    .content .main_content .right .grid_img p,
    .content .main_content .right .bottom.grid_img p,
    .grid_img a p {
        position: static !important;
        display: block !important;
        width: 100% !important;
        margin: 8px 0 0 0 !important;
        margin-left: 0 !important;
        margin-top: 8px !important;
        font-size: 14px !important;
        font-weight: 500 !important;
        text-align: center !important;
    }
}

/* ==========================================================================
   移动端手机核心适配 (<= 768px)
   ========================================================================== */
@media screen and (max-width: 768px) {
    /* 1. 全局容器与Body */
    html, body {
        width: 100% !important;
        max-width: 100% !important;
        overflow-x: hidden !important;
    }

    body {
        min-width: 0 !important;
        height: auto !important;
        min-height: 100vh !important;
        margin: 0 !important;
        padding: 0 !important;
        background-color: #f8fafc !important;
    }

    /* 限制 content 内部所有元素绝不超出父容器 */
    .content, .content * {
        max-width: 100% !important;
        box-sizing: border-box !important;
    }

    /* 2. 头部Header：消除原背景图与文字挤压 */
    .header {
        width: 100% !important;
        height: auto !important;
        min-height: 52px !important;
        padding: 6px 10px !important;
        display: flex !important;
        justify-content: space-between !important;
        align-items: center !important;
        background: #2a6dbb !important;
        background-image: none !important;
        border-bottom: 3px solid #fd7d02 !important;
        margin-top: 0 !important;
        overflow: hidden !important;
    }

    .header .logo {
        margin: 0 !important;
        flex: 1 1 auto !important;
        max-width: 65% !important;
    }

    .header .logo img {
        position: static !important;
        height: 34px !important;
        width: auto !important;
        display: block !important;
        object-fit: contain !important;
    }

    .header .school {
        position: static !important;
        float: none !important;
        margin: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-end !important;
        font-size: 12px !important;
        color: #fff !important;
        white-space: nowrap !important;
        flex: 0 0 auto !important;
        gap: 3px !important;
    }

    .header .school a {
        font-size: 12px !important;
        color: #ffffff !important;
        padding: 2px 2px !important;
    }

    .header .school p {
        color: rgba(255,255,255,0.7) !important;
        margin: 0 !important;
    }

    /* 3. 导航栏Nav：横向平滑触摸滚动，全站6大主栏目完整展现 */
    .nav {
        width: 100% !important;
        max-width: 100% !important;
        height: 42px !important;
        background-color: #1e5597 !important;
        overflow-x: auto !important;
        overflow-y: hidden !important;
        -webkit-overflow-scrolling: touch !important;
        scrollbar-width: none !important;
        border-radius: 0 !important;
        position: relative !important;
        top: 0 !important;
        left: 0 !important;
        transform: none !important;
        z-index: 100 !important;
    }

    .nav::-webkit-scrollbar {
        display: none !important;
    }

    .nav ul {
        display: inline-flex !important;
        flex-wrap: nowrap !important;
        width: max-content !important;
        max-width: none !important;
        height: 42px !important;
        padding: 0 8px !important;
        margin: 0 !important;
    }

    .nav li {
        width: auto !important;
        min-width: max-content !important;
        max-width: none !important;
        padding: 0 12px !important;
        margin: 0 1px !important;
        height: 42px !important;
        line-height: 42px !important;
        flex-shrink: 0 !important;
    }

    .nav li a {
        font-size: 14px !important;
        white-space: nowrap !important;
        display: block !important;
        color: #ffffff !important;
        padding: 0 !important;
    }

    .nav .down_list ul {
        display: none !important;
    }

    /* 4. 二级页面结构核心降维 (解除绝对定位) */
    .content {
        position: static !important;
        top: auto !important;
        left: auto !important;
        width: 95% !important;
        margin: 12px auto 25px auto !important;
        padding: 0 !important;
        height: auto !important;
        min-height: auto !important;
    }

    .content .title {
        position: static !important;
        top: auto !important;
        left: auto !important;
        width: 100% !important;
        height: auto !important;
        line-height: 1.5 !important;
        padding: 6px 2px !important;
        margin: 0 0 10px 0 !important;
        display: flex !important;
        align-items: center !important;
        flex-wrap: wrap !important;
        gap: 4px !important;
        font-size: 12px !important;
        color: #64748b !important;
        border-bottom: 1px solid #e2e8f0 !important;
    }

    .content .title img {
        position: static !important;
        margin: 0 !important;
        height: 13px !important;
        width: auto !important;
        vertical-align: middle !important;
    }

    .content .title a {
        color: #2563eb !important;
        font-size: 12px !important;
        margin: 0 !important;
    }

    .content .title .main {
        margin-left: 2px !important;
    }

    .content .main_content {
        position: static !important;
        top: auto !important;
        left: auto !important;
        width: 100% !important;
        height: auto !important;
        display: flex !important;
        flex-direction: column !important;
        gap: 12px !important;
    }

    /* 侧边栏/分类项转为手机自适应优雅标签 */
    .content .main_content .left {
        position: static !important;
        top: auto !important;
        left: auto !important;
        width: 100% !important;
        min-width: 100% !important;
        height: auto !important;
        margin: 0 !important;
        padding: 10px 12px !important;
        background: #ffffff !important;
        border-radius: 8px !important;
        box-shadow: 0 1px 4px rgba(0,0,0,0.05) !important;
    }

    .content .main_content .left .achievements,
    .content .main_content .left .team,
    .content .main_content .left .recruit {
        width: 100% !important;
        margin: 0 0 8px 0 !important;
        height: 30px !important;
        line-height: 30px !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        color: #1e3a8a !important;
        background: #eff6ff !important;
        border-radius: 4px !important;
        padding-left: 8px !important;
        text-align: left !important;
    }

    .content .main_content .left ul {
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 4px !important;
        padding: 0 !important;
        margin: 0 !important;
        width: 100% !important;
    }

    .content .main_content .left li:not(.achievements_son):not(.achievements):not(.team):not(.recruit) {
        width: auto !important;
        height: auto !important;
        margin: 0 !important;
        line-height: normal !important;
    }

    .content .main_content .left li:not(.achievements_son) a {
        padding: 5px 10px !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        border-radius: 4px !important;
        background-color: #f1f5f9 !important;
        color: #334155 !important;
        display: inline-block !important;
        text-align: center !important;
    }

    .content .main_content .left li:not(.achievements_son) a.selected,
    .content .main_content .left li:not(.achievements_son) .selected {
        background-color: #2563eb !important;
        color: #ffffff !important;
    }

    /* 年份标签(.achievements_son)精美时间轴栅格化 (5列均分排列) */
    .content .main_content .left .achievements_son {
        display: inline-block !important;
        width: calc(20% - 4px) !important;
        min-width: 0 !important;
        height: 26px !important;
        line-height: 26px !important;
        margin: 2px !important;
        padding: 0 !important;
        background: transparent !important;
    }

    .content .main_content .left .achievements_son a {
        display: block !important;
        width: 100% !important;
        height: 26px !important;
        line-height: 24px !important;
        padding: 0 !important;
        font-size: 12px !important;
        border-radius: 4px !important;
        background-color: #f8fafc !important;
        border: 1px solid #e2e8f0 !important;
        color: #64748b !important;
        text-align: center !important;
    }

    .content .main_content .left .achievements_son a.selected,
    .content .main_content .left .achievements_son .selected {
        background-color: #3b82f6 !important;
        color: #ffffff !important;
        border-color: #2563eb !important;
    }

    /* 正文内容卡片：解除固定尺寸，取消overflow:hidden */
    .content .main_content .right {
        position: static !important;
        top: auto !important;
        left: auto !important;
        width: 100% !important;
        min-width: 0 !important;
        height: auto !important;
        border-left: none !important;
        padding: 14px 10px !important;
        background: #ffffff !important;
        border-radius: 8px !important;
        box-shadow: 0 1px 4px rgba(0,0,0,0.05) !important;
        overflow: visible !important;
    }

    .content .main_content .right .top,
    .content .main_content .right .topzhuanli {
        width: 100% !important;
        height: auto !important;
        line-height: normal !important;
        text-align: left !important;
        margin: 0 0 12px 0 !important;
        padding: 0 0 6px 0 !important;
        border-left: none !important;
        border-bottom: 2px solid #2563eb !important;
    }

    .content .main_content .right .top h2,
    .content .main_content .right .topzhuanli h2,
    .content .main_content .right .h2 {
        font-size: 17px !important;
        font-weight: 700 !important;
        color: #1e3a8a !important;
        margin: 0 !important;
    }

    .content .main_content .right .bottom,
    .content .main_content .right .bottomjijin {
        width: 100% !important;
        height: auto !important;
        min-height: 0 !important;
        border-left: none !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* 论文、专利和项目条目：标准英文断行排版，永不截断 */
    .content .main_content .right .bottom .lunwenStyle,
    .content .main_content .right .bottom a,
    .content .main_content .right .bottomjijin a {
        display: block !important;
        width: 100% !important;
        height: auto !important;
        min-height: 0 !important;
        font-size: 13.5px !important;
        font-weight: 600 !important;
        line-height: 1.55 !important;
        margin: 14px 0 4px 0 !important;
        padding: 0 !important;
        border: none !important;
        text-indent: 0 !important;
        color: #1e293b !important;
        word-break: normal !important;
        overflow-wrap: break-word !important;
        white-space: normal !important;
    }

    .content .main_content .right .bottom div,
    .content .main_content .right .bottom .journal,
    .content .main_content .right .bottom .DOI {
        display: block !important;
        width: 100% !important;
        height: auto !important;
        padding: 0 !important;
        margin: 3px 0 !important;
        font-size: 12.5px !important;
        line-height: 1.5 !important;
        text-indent: 0 !important;
        word-break: normal !important;
        overflow-wrap: break-word !important;
        white-space: normal !important;
        color: #475569 !important;
    }

    .content .main_content .right .bottom .DOI {
        color: #2563eb !important;
        word-break: break-all !important;
        padding-bottom: 8px !important;
        margin-bottom: 8px !important;
        border-bottom: 1px dashed #e2e8f0 !important;
    }

    /* 新闻动态列表：清除原 CSS 带来的 margin-left: 35px 与 width: 103% */
    .content .main_content .right .bottom ul {
        padding: 0 !important;
        margin: 0 !important;
        width: 100% !important;
    }

    .content .main_content .right .bottom li {
        width: 100% !important;
        height: auto !important;
        min-height: 40px !important;
        margin: 8px 0 !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
        padding: 6px 0 !important;
        background: transparent !important;
        border-bottom: 1px dashed #e2e8f0 !important;
        list-style: none !important;
    }

    .content .bottom a p,
    .content .bottom a span {
        float: none !important;
        display: block !important;
        width: 100% !important;
        margin: 2px 0 !important;
        padding: 0 !important;
        word-break: normal !important;
        overflow-wrap: break-word !important;
    }

    .content .bottom a span {
        font-size: 12px !important;
        color: #94a3b8 !important;
    }

    /* 成员网格列表：2列紧凑自适应卡片 */
    .content .main_content .right .grid_img,
    .content .main_content .right .bottom.grid_img,
    .grid_img {
        display: grid !important;
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 12px !important;
        width: 100% !important;
        height: auto !important;
        min-height: 0 !important;
        margin: 8px 0 !important;
        padding: 0 !important;
        border-left: none !important;
    }

    .content .main_content .right .grid_img a,
    .content .main_content .right .bottom.grid_img a,
    .grid_img a {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: flex-start !important;
        width: 100% !important;
        height: auto !important;
        min-height: 0 !important;
        margin: 0 !important;
        margin-top: 0 !important;
        padding: 10px 4px !important;
        background: #f8fafc !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
        text-decoration: none !important;
    }

    .content .main_content .right .grid_img a img,
    .content .main_content .right .grid_img img,
    .content .main_content .right .bottom.grid_img img,
    .grid_img a img {
        position: static !important;
        display: block !important;
        width: 105px !important;
        height: 140px !important;
        max-width: 85% !important;
        max-height: 140px !important;
        object-fit: cover !important;
        border-radius: 6px !important;
        margin: 0 auto !important;
        padding: 0 !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.08) !important;
    }

    .content .main_content .right .grid_img a p,
    .content .main_content .right .grid_img p,
    .content .main_content .right .bottom.grid_img p,
    .grid_img a p {
        position: static !important;
        display: block !important;
        width: 100% !important;
        margin: 8px 0 0 0 !important;
        margin-top: 8px !important;
        margin-left: 0 !important;
        margin-right: 0 !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        color: #1e293b !important;
        text-align: center !important;
        line-height: 1.3 !important;
        padding: 0 !important;
    }

    /* 师生个人详情页 (刘爱萍教授等介绍) */
    .content .main_content .right .student,
    .student, .content .pic {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        width: 100% !important;
        height: auto !important;
        margin: 8px 0 !important;
        padding: 0 !important;
    }

    .content .main_content .right .student img,
    .student p img, .student img {
        position: static !important;
        display: block !important;
        margin: 8px auto 14px auto !important;
        width: 150px !important;
        max-width: 65% !important;
        height: auto !important;
        border-radius: 8px !important;
        box-shadow: 0 3px 8px rgba(0,0,0,0.12) !important;
    }

    .content .main_content .right .student p,
    .student p {
        width: 100% !important;
        margin: 6px 0 !important;
        padding: 0 !important;
        text-indent: 2em !important;
        font-size: 14px !important;
        line-height: 1.8 !important;
        color: #334155 !important;
        word-break: break-word !important;
        overflow-wrap: break-word !important;
        text-align: justify !important;
    }

    .content .main_content .right .student h3,
    .content .main_content .right .student h2 {
        text-align: center !important;
        margin: 8px 0 !important;
        font-size: 17px !important;
        font-weight: bold !important;
    }

    /* 分页条控件 (重置绝对定位) */
    .content .main_content .right .change_page {
        position: static !important;
        width: 100% !important;
        height: auto !important;
        margin: 16px 0 6px 0 !important;
        padding: 8px 0 !important;
        border-top: 1px solid #e5e7eb !important;
        display: flex !important;
        justify-content: center !important;
    }

    .content .main_content .right .change_page div {
        width: 100% !important;
    }

    .content .main_content .right .change_page ul {
        display: flex !important;
        justify-content: center !important;
        flex-wrap: wrap !important;
        gap: 6px !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    .content .main_content .right .change_page li {
        position: static !important;
        left: auto !important;
        top: auto !important;
        width: 32px !important;
        height: 32px !important;
        line-height: 32px !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 4px !important;
        background: #ffffff !important;
        margin: 0 !important;
    }

    .content .main_content .right .change_page li a {
        width: 100% !important;
        height: 100% !important;
        line-height: 32px !important;
        text-align: center !important;
        font-size: 13px !important;
        color: #334155 !important;
    }

    .content .main_content .right .change_page li.selected,
    .content .main_content .right .change_page .selected {
        background-color: #2563eb !important;
        border-color: #2563eb !important;
    }

    .content .main_content .right .change_page li.selected a,
    .content .main_content .right .change_page .selected a {
        color: #ffffff !important;
    }

    /* 移动端禁用滚动吸顶JS的定位破坏 */
    .leffix {
        position: static !important;
        width: 100% !important;
        top: auto !important;
        animation: none !important;
    }

    .nav.fix {
        position: static !important;
        width: 100% !important;
        left: auto !important;
        transform: none !important;
        animation: none !important;
    }

    .nav2, .lef2 {
        margin-top: 0 !important;
    }

    /* 5. 首页单列上下排布，彻底消除左右两半撕裂 */
    .index_row_section {
        display: flex !important;
        flex-direction: column !important;
        width: 100% !important;
        height: auto !important;
        margin-top: 8px !important;
    }

    .col_home, .col_about, .col_news, .col_gallery {
        width: 100% !important;
        height: auto !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* 标题小横条 */
    .all_title {
        display: block !important;
        width: 92% !important;
        margin: 15px auto 6px auto !important;
    }

    .homepage_title, .about_us, .news {
        width: 100% !important;
        height: 32px !important;
        margin: 0 !important;
        border-bottom: 1px solid #d1d5db !important;
    }

    .homepage_title p, .about_us p, .news p {
        width: auto !important;
        height: 32px !important;
        display: inline-block !important;
        border-bottom: 2px solid #2563eb !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        color: #1f2937 !important;
        padding-right: 12px !important;
        margin: 0 !important;
    }

    /* 轮播图模块 */
    .banners {
        position: relative !important;
        left: 0 !important;
        width: 92% !important;
        max-width: 100% !important;
        height: 220px !important;
        margin: 8px auto 14px auto !important;
        border-radius: 8px !important;
        overflow: hidden !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08) !important;
    }

    .banners img {
        width: 100% !important;
        height: 220px !important;
        object-fit: cover !important;
        border-radius: 8px !important;
    }

    .images {
        height: 220px !important;
        max-width: none !important;
    }

    /* 课题组简介正文 */
    .about_us_content {
        position: static !important;
        width: 92% !important;
        height: auto !important;
        margin: 8px auto 20px auto !important;
        text-indent: 2em !important;
    }

    .about_us_content p {
        font-size: 15px !important;
        line-height: 1.8 !important;
        color: #374151 !important;
        margin-bottom: 10px !important;
    }

    /* 实验室动态新闻列表 */
    .bannersall.new__ {
        position: static !important;
        width: 92% !important;
        height: auto !important;
        margin: 8px auto !important;
        overflow: visible !important;
        border-radius: 0 !important;
        box-shadow: none !important;
    }

    .new__ ul {
        padding: 0 !important;
        margin: 0 !important;
    }

    .new__ li {
        width: 100% !important;
        height: auto !important;
        margin: 0 0 10px 0 !important;
        padding: 8px 0 !important;
        line-height: 1.5 !important;
        list-style: none !important;
        border-bottom: 1px dashed #e5e7eb !important;
        background: transparent !important;
    }

    .new__ a {
        display: flex !important;
        flex-direction: column !important;
        width: 100% !important;
        height: auto !important;
        padding: 0 !important;
        font-size: 14px !important;
        color: #1f2937 !important;
    }

    .new__ p {
        width: 100% !important;
        white-space: normal !important;
        line-height: 1.5 !important;
        margin: 0 0 4px 0 !important;
    }

    .new__ span {
        margin: 0 !important;
        font-size: 12px !important;
        color: #9ca3af !important;
    }

    /* 课余生活相册预览卡片 */
    #previewContainer {
        width: 92% !important;
        max-width: 360px !important;
        height: 200px !important;
        margin: 10px auto 25px auto !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.12) !important;
    }

    /* 6. 页脚Tail移动端整齐居中，消除重叠 */
    .tail {
        width: 100% !important;
        margin-top: 30px !important;
        padding: 20px 15px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        text-align: center !important;
        background-color: #2a6dbb !important;
    }

    .tail .logo {
        margin: 0 0 12px 0 !important;
    }

    .tail .logo img {
        height: 55px !important;
        width: auto !important;
    }

    .tail .info {
        margin: 0 !important;
        width: 100% !important;
        text-align: center !important;
        font-size: 12px !important;
        line-height: 1.6 !important;
    }

    .tail .info p, .tail .info a {
        margin: 3px 0 !important;
        margin-left: 0 !important;
        font-size: 12px !important;
        word-break: break-all !important;
    }

    /* 7. AI 助手悬浮挂件手机端优化 */
    #ai-float-button {
        bottom: 20px !important;
        right: 20px !important;
        width: 48px !important;
        height: 48px !important;
    }

    #ai-chat-window {
        width: calc(100vw - 20px) !important;
        right: 10px !important;
        bottom: 78px !important;
        height: 500px !important;
        max-height: 75vh !important;
    }
}
"""

with open(CSS_PATH, "w", encoding="utf-8") as f:
    f.write(new_responsive)

print("responsive.css updated successfully with .content, .content * max-width: 100% constraint.")
