/**
 * Cloudflare Worker AI 代理服务代码
 * 部署至 Cloudflare Workers (绑定域名如 api.yes.lzh1.eu.org)
 * 
 * 模型已更新为: @cf/qwen/qwen3.8-27b
 */

// 默认使用的 AI 模型
const DEFAULT_MODEL = '@cf/qwen/qwen3.8-27b';

// 如果通过 HTTP API 转发（无 env.AI 绑定时使用的凭据）
const CF_ACCOUNT_ID = '371438b5dba15161c6ef55a3884a1c7b';
const CF_API_TOKEN = 'yO9DSWAzOBGOQ189KUUB45dFNLhli05vtQtQPi5T';

export default {
    async fetch(request, env, ctx) {
        // 1. 处理 CORS 跨域预检请求
        if (request.method === 'OPTIONS') {
            return new Response(null, {
                status: 204,
                headers: {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
                    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
                    'Access-Control-Max-Age': '86400',
                }
            });
        }

        // 2. 只处理 POST 请求
        if (request.method !== 'POST') {
            return new Response(JSON.stringify({ error: 'Method not allowed' }), {
                status: 405,
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            });
        }

        try {
            const body = await request.json();
            const messages = body.messages || [];
            const targetModel = body.model || DEFAULT_MODEL;

            let responseData;

            // 方式 A: 如果 Worker 绑定了原生 Workers AI 模块 (env.AI)
            if (env && env.AI) {
                const aiResult = await env.AI.run(targetModel, {
                    messages: messages,
                    max_tokens: body.max_tokens || 1024,
                    temperature: body.temperature || 0.7,
                });
                responseData = {
                    result: aiResult,
                    success: true
                };
            } else {
                // 方式 B: 通过 Cloudflare REST API 请求
                const accountId = (env && env.ACCOUNT_ID) || CF_ACCOUNT_ID;
                const apiToken = (env && env.API_TOKEN) || CF_API_TOKEN;

                const cfApiUrl = `https://api.cloudflare.com/client/v4/accounts/${accountId}/ai/run/${targetModel}`;

                const cfResponse = await fetch(cfApiUrl, {
                    method: 'POST',
                    headers: {
                        'Authorization': `Bearer ${apiToken}`,
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        messages: messages,
                        max_tokens: body.max_tokens || 1024,
                        temperature: body.temperature || 0.7
                    })
                });

                responseData = await cfResponse.json();
            }

            // 返回结果并附加 CORS 响应头
            return new Response(JSON.stringify(responseData), {
                status: 200,
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'Content-Type, Authorization'
                }
            });

        } catch (error) {
            return new Response(JSON.stringify({
                success: false,
                error: error.message || 'Worker Internal Error'
            }), {
                status: 500,
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            });
        }
    }
};
