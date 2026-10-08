# -*- coding: utf-8 -*-
import subprocess, time, urllib.request, json, asyncio
try:
    import websockets
except ImportError:
    import os
    os.system("pip install websockets")
    import websockets

async def check_dom():
    p = subprocess.Popen([
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "--headless",
        "--disable-gpu",
        "--remote-debugging-port=9223",
        "--window-size=375,812",
        "http://localhost:8000/4.1.2026.html"
    ])
    await asyncio.sleep(2)
    try:
        tabs = json.loads(urllib.request.urlopen("http://localhost:9223/json").read())
        ws_url = tabs[0]["webSocketDebuggerUrl"]
        async with websockets.connect(ws_url) as ws:
            js_code = """
            (() => {
                const elNames = ['html', 'body', '.content', '.main_content', '.left', '.right', '.bottom', '.lunwenStyle'];
                const results = {};
                for (const sel of elNames) {
                    const el = document.querySelector(sel);
                    if (el) {
                        const rect = el.getBoundingClientRect();
                        const comp = window.getComputedStyle(el);
                        results[sel] = {
                            width: rect.width,
                            left: rect.left,
                            right: rect.right,
                            cssWidth: comp.width,
                            maxWidth: comp.maxWidth,
                            paddingLeft: comp.paddingLeft,
                            paddingRight: comp.paddingRight,
                            marginLeft: comp.marginLeft,
                            marginRight: comp.marginRight,
                            overflow: comp.overflow,
                            position: comp.position
                        };
                    } else {
                        results[sel] = 'NOT_FOUND';
                    }
                }
                return results;
            })()
            """
            req = {
                "id": 1,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": js_code,
                    "returnByValue": True
                }
            }
            await ws.send(json.dumps(req))
            res = await ws.recv()
            data = json.loads(res)
            print(json.dumps(data["result"]["result"]["value"], indent=2, ensure_ascii=False))
    finally:
        p.kill()

if __name__ == "__main__":
    asyncio.run(check_dom())
