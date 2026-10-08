# -*- coding: utf-8 -*-
import subprocess
import time
import json
from http.server import HTTPServer, SimpleHTTPRequestHandler

result_data = None

class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        global result_data
        if self.path == '/overflow':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            result_data = json.loads(post_data.decode('utf-8'))
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            super().do_POST()

server = HTTPServer(('127.0.0.1', 8889), Handler)

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
            var cs = window.getComputedStyle(el);
            var scrollWidth = el.scrollWidth;
            var offsetWidth = el.offsetWidth;
            var clientWidth = el.clientWidth;
            // Check if element itself has min-width, width, or children forcing it wide
            if (scrollWidth > 375 || offsetWidth > 375) {
                items.push({
                    selector: el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (el.className ? '.' + el.className.split(' ').join('.') : ''),
                    scrollWidth: scrollWidth,
                    offsetWidth: offsetWidth,
                    clientWidth: clientWidth,
                    css_width: cs.width,
                    css_min_width: cs.minWidth,
                    css_max_width: cs.maxWidth,
                    css_overflow: cs.overflow,
                    css_overflow_x: cs.overflowX,
                    css_white_space: cs.whiteSpace
                });
            }
        }
        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'http://127.0.0.1:8889/overflow', true);
        xhr.send(JSON.stringify(items));
    }, 500);
});
</script>
"""

with open('debug_inspect2.html', 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', inspector + '</body>'))

cmd = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "--headless",
    "--disable-gpu",
    "--window-size=375,1000",
    "http://127.0.0.1:8889/debug_inspect2.html"
]
proc = subprocess.Popen(cmd)

start = time.time()
while time.time() - start < 10 and result_data is None:
    server.handle_request()

proc.kill()

for item in result_data or []:
    print(f"{item['selector']:40} scrollW={item['scrollWidth']:3} offsetW={item['offsetWidth']:3} css_w={item['css_width']:10} min_w={item['css_min_width']:10}")
