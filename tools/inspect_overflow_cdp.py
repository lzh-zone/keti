# -*- coding: utf-8 -*-
import subprocess
import time
import json
import urllib.request
import asyncio
import sys

# We can also just use playwright if installed or simple CDP via standard library or a simple html injection.
# Actually, why not just inject a script into test.html that writes the result to a file using fetch to a simple python server?
# That's 10 lines of python and 100% works!

from http.server import HTTPServer, SimpleHTTPRequestHandler

overflow_data = None

class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        global overflow_data
        if self.path == '/overflow':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            overflow_data = json.loads(post_data.decode('utf-8'))
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            super().do_POST()

server = HTTPServer(('127.0.0.1', 8888), Handler)

# Create test page with inspector
with open('4.1.2026.html', 'r', encoding='utf-8') as f:
    html = f.read()

inspector = """
<script>
window.addEventListener('load', function() {
    setTimeout(function() {
        var items = [];
        var all = document.querySelectorAll('*');
        for (var i = 0; i < all.length; i++) {
            var el = all[i];
            var r = el.getBoundingClientRect();
            var cs = window.getComputedStyle(el);
            if (r.width > 375 || r.right > 375 || (r.left + r.width) > 375) {
                items.push({
                    tag: el.tagName,
                    cls: el.className,
                    id: el.id,
                    w: Math.round(r.width),
                    left: Math.round(r.left),
                    right: Math.round(r.right),
                    css_w: cs.width,
                    css_max_w: cs.maxWidth,
                    css_box_sizing: cs.boxSizing,
                    parent_tag: el.parentElement ? el.parentElement.tagName : null,
                    parent_cls: el.parentElement ? el.parentElement.className : null
                });
            }
        }
        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'http://127.0.0.1:8888/overflow', true);
        xhr.send(JSON.stringify(items));
    }, 500);
});
</script>
"""

with open('debug_inspect.html', 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', inspector + '</body>'))

# Launch browser in separate process
cmd = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "--headless",
    "--disable-gpu",
    "--window-size=375,1000",
    "http://127.0.0.1:8888/debug_inspect.html"
]
proc = subprocess.Popen(cmd)

start = time.time()
while time.time() - start < 10 and overflow_data is None:
    server.handle_request()

proc.kill()

print("RESULTS COUNT:", len(overflow_data) if overflow_data else 0)
if overflow_data:
    for item in overflow_data:
        print(f"[{item['tag']}.{item['cls']}] width={item['w']}, left={item['left']}, right={item['right']}, css_w={item['css_w']}, box_sizing={item['css_box_sizing']}, parent={item['parent_tag']}.{item['parent_cls']}")
