# AI 助手部署说明

## 概述

本项目的 AI 助手功能通过 **CORS 代理服务** (corsproxy.io) 调用 Cloudflare AI API,适用于 GitHub Pages 等静态托管平台。

## 当前配置

✅ **已配置 CORS 代理**

代码使用 `https://corsproxy.io/` 作为代理,自动处理跨域请求:

```javascript
apiUrl: 'https://corsproxy.io/?' + encodeURIComponent('https://api.cloudflare.com/...')
```

这样可以直接在 GitHub Pages 上使用,无需额外配置。

## 使用说明

1. **部署到 GitHub Pages**
   - 将代码推送到 GitHub 仓库
   - 在仓库设置中启用 GitHub Pages
   - 访问您的网站 URL

2. **测试 AI 助手**
   - 点击页面右下角的 AI 助手悬浮按钮
   - 在聊天窗口输入问题
   - 等待 AI 回复

## 注意事项

> **⚠️ 公共代理服务限制**
> 
> - `corsproxy.io` 是免费的公共服务,可能有速率限制
> - API Token 会暴露在前端代码中(任何人都可以查看)
> - 不建议用于高流量或敏感应用

## 替代方案

如果需要更好的性能和安全性,建议使用:

### 方案 1: Cloudflare Workers(推荐)

创建自己的 Worker 代理,隐藏 API Token:
1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. 创建 Worker(免费,每天 10 万次请求)
3. 将 Worker URL 更新到 `js/ai-assistant.js`

### 方案 2: Vercel/Netlify

部署到支持 Serverless Functions 的平台。

## 本地测试

如需本地测试,可以:

1. **直接打开 HTML 文件**
   ```
   双击 index.html
   ```

2. **或使用本地服务器**
   ```bash
   python api-proxy.py
   # 访问 http://localhost:8000
   ```

## 文件说明

- `js/ai-assistant.js` - AI 助手前端代码(已配置 CORS 代理)
- `css/ai-assistant.css` - AI 助手样式
- `api-proxy.py` - 本地开发用代理服务器(可选)