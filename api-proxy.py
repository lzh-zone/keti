#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的 API 代理服务器
用于解决 CORS 问题,将浏览器请求转发到 Cloudflare AI API
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import urllib.request
import urllib.error

API_URL = 'https://api.cloudflare.com/client/v4/accounts/371438b5dba15161c6ef55a3884a1c7b/ai/run/@cf/meta/llama-3-8b-instruct'
API_TOKEN = 'yO9DSWAzOBGOQ189KUUB45dFNLhli05vtQtQPi5T'

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # 添加 CORS 头
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        SimpleHTTPRequestHandler.end_headers(self)
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()
    
    def do_POST(self):
        # 只处理 /api/chat 路径
        if self.path == '/api/chat':
            try:
                # 读取请求体
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                request_data = json.loads(post_data.decode('utf-8'))
                
                print(f'收到请求: {request_data}')
                
                # 转发到 Cloudflare API
                req = urllib.request.Request(
                    API_URL,
                    data=json.dumps(request_data).encode('utf-8'),
                    headers={
                        'Authorization': f'Bearer {API_TOKEN}',
                        'Content-Type': 'application/json'
                    },
                    method='POST'
                )
                
                # 发送请求
                with urllib.request.urlopen(req) as response:
                    response_data = response.read()
                    print(f'API 响应: {response_data.decode("utf-8")}')
                    
                    # 返回响应
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(response_data)
                    
            except urllib.error.HTTPError as e:
                error_body = e.read().decode('utf-8')
                print(f'API 错误: {e.code} - {error_body}')
                self.send_response(e.code)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(error_body.encode('utf-8'))
                
            except Exception as e:
                print(f'服务器错误: {str(e)}')
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                error_response = json.dumps({'error': str(e)})
                self.wfile.write(error_response.encode('utf-8'))
        else:
            # 其他路径使用默认处理
            SimpleHTTPRequestHandler.do_POST(self)

if __name__ == '__main__':
    port = 8000
    server = HTTPServer(('localhost', port), CORSRequestHandler)
    print(f'🚀 服务器启动成功!')
    print(f'📡 访问地址: http://localhost:{port}')
    print(f'🤖 API 代理已启用: /api/chat')
    print(f'按 Ctrl+C 停止服务器')
    print('-' * 50)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n服务器已停止')
        server.shutdown()
