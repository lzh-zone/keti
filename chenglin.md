# 静态网站迁移到 Hexo 指南

## 准备工作

1. 确保已安装 Node.js 和 npm
2. 全局安装 Hexo：
   ```bash
   npm install -g hexo-cli
   ```

## 创建新的 Hexo 项目

1. 创建新的 Hexo 项目：
   ```bash
   hexo init my-blog
   cd my-blog
   ```

2. 安装依赖：
   ```bash
   npm install
   ```

## 迁移静态资源

1. 将原项目的静态资源迁移到对应目录：
   - CSS 文件 → `source/css/`
   - JavaScript 文件 → `source/js/`
   - 图片文件 → `source/images/`
   - 其他静态资源 → `source/static/`

2. 在 `_config.yml` 中配置资源目录：
   ```yaml
   source_dir: source
   public_dir: public
   ```

## 迁移 HTML 内容

1. 将 `1.index.html` 的内容转换为 Markdown 格式，保存为 `source/_posts/index.md`
2. 其他 HTML 页面也转换为 Markdown 格式，放在 `source/_posts/` 目录下

## 配置主题

1. 选择一个 Hexo 主题（如 landscape）：
   ```bash
   npm install hexo-theme-landscape
   ```

2. 在 `_config.yml` 中配置主题：
   ```yaml
   theme: landscape
   ```

## 自定义样式

1. 在 `source/css/` 目录下创建 `custom.css`
2. 在主题配置文件中引入自定义样式

## 部署

1. 生成静态文件：
   ```bash
   hexo generate
   ```

2. 本地预览：
   ```bash
   hexo server
   ```

3. 部署到服务器（可选）：
   ```bash
   hexo deploy
   ```

## 注意事项

1. 确保所有相对路径都正确更新
2. 检查所有资源文件的引用路径
3. 测试所有功能是否正常工作
4. 备份原始文件，直到确认迁移成功

## 常见问题解决

1. 如果遇到路径问题，检查 `_config.yml` 中的配置
2. 如果样式不生效，检查 CSS 文件的引入方式
3. 如果图片不显示，检查图片路径是否正确

## 后续优化

1. 添加 SEO 优化
2. 配置评论系统
3. 添加统计功能
4. 优化加载速度

## 参考资源

- [Hexo 官方文档](https://hexo.io/zh-cn/docs/)
- [Hexo 主题列表](https://hexo.io/themes/)
- [Markdown 语法指南](https://www.markdownguide.org/)

---
title: 程琳
layout: page
css: 3.team_intro.css
---

<div class="main_content" style="position: relative; width: 100%; min-height: 1200px; z-index: 0;">
    <!-- Left Sidebar -->
    <div class="left" id="lef__" style="width: 230px; position: absolute; top: 0; left: 0;">
        <ul style="list-style: none; padding: 0;">
            <li class="team" style="height: 53px; width: 230px; margin-top: 0; line-height: 53px; text-align: center; font-family: 微软雅黑; background: url(/images/content_background.png) no-repeat 0 0; color: white; font-size: 20px;">
                <a href="/team" style="color: #FFFFFF; display: block;">研究团队</a>
            </li>
            <li style="height: 53px; width: 230px; background-color: #f5f6fa; text-align: center; line-height: 53px; margin: 7px 0;">
                <a href="/team/teachers" style="display: block; color: #666666; transition: .3s; background-color: #0b6cb8; color: white;">团队老师</a>
            </li>
            <li style="height: 53px; width: 230px; background-color: #f5f6fa; text-align: center; line-height: 53px; margin: 7px 0;">
                <a href="/team/phd" style="display: block; color: #666666; transition: .3s;">博士研究生</a>
            </li>
            <li style="height: 53px; width: 230px; background-color: #f5f6fa; text-align: center; line-height: 53px; margin: 7px 0;">
                <a href="/team/master" style="display: block; color: #666666; transition: .3s;">硕士研究生</a>
            </li>
            <li style="height: 53px; width: 230px; background-color: #f5f6fa; text-align: center; line-height: 53px; margin: 7px 0;">
                <a href="/team/alumni" style="display: block; color: #666666; transition: .3s;">已毕业学生</a>
            </li>
        </ul>
    </div>

    <!-- Right Content -->
    <div class="right" style="position: relative; margin-left: 240px; width: calc(100% - 240px); z-index: 999;">
        <div class="top" style="width: 100%; height: 80px; line-height: 80px; text-align: center; border-bottom: 1px dashed #eee; border-left: 1px dashed #eee;">
            <h2 style="font-weight: 500; font-size: 30px; font-family: 楷体; font-weight: normal;">程琳</h2>
        </div>
        <div class="student" style="width: 100%; text-align: left; padding: 20px;">
            <p style="text-indent: 0;"><img src="/images/pictures/chenglin.jpg" alt="" style="height: 300px; margin-left: 28.5%;"></p>
            <p style="margin-top: 20px; text-indent: 0; font-size: 19px; font-family: 微软雅黑; margin: 20px 0; line-height: 32px;"><b>教师简介</b></p>
            <p style="font-size: 19px; font-family: 微软雅黑; margin: 20px 0; text-indent: 37px; line-height: 32px;">程琳，女，博士，浙江理工大学，理学院物理系，实验师。主持国家自然科学基金青年项目1项，浙江省自然科学基金青年探索项目1项，参与国家自然科学基金面上项目2项。在Nano Energy，Journal of Materials Chemistry C，IEEE Sensors Journal等高水平期刊上发表 SCI论文 20 余篇，授权国家发明专利 20 余项，指导学生获国家级省级竞赛获奖 10 余项。</p>
            <p style="text-indent: 0; font-size: 19px; font-family: 微软雅黑; margin: 20px 0; line-height: 32px;"><b>研究领域及研究方向</b></p>
            <p style="font-size: 19px; font-family: 微软雅黑; margin: 20px 0; text-indent: 37px; line-height: 32px;">1.柔性可穿戴智能传感器的设计及其在人机交互中的应用研究；</p>
            <p style="font-size: 19px; font-family: 微软雅黑; margin: 20px 0; text-indent: 37px; line-height: 32px;">2.物理实验教学与仪器开发。</p>
        </div>
    </div>
</div> 