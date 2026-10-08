import subprocess, time, json
from http.server import HTTPServer, SimpleHTTPRequestHandler

data = None
class H(SimpleHTTPRequestHandler):
    def do_POST(self):
        global data
        data = self.rfile.read(int(self.headers['Content-Length'])).decode()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

s = HTTPServer(('127.0.0.1', 8890), H)
with open('debug_dim.html', 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html>
<head><meta name="viewport" content="width=device-width, initial-scale=1.0"></head>
<body>
<script>
fetch("http://127.0.0.1:8890/dim", {
    method:"POST", 
    body: JSON.stringify({
        innerW: window.innerWidth, 
        innerH: window.innerHeight, 
        outerW: window.outerWidth, 
        docW: document.documentElement.clientWidth, 
        bodyW: document.body.clientWidth
    })
});
</script>
</body>
</html>''')

p = subprocess.Popen([r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe', '--headless', '--disable-gpu', '--window-size=375,1000', 'http://127.0.0.1:8890/debug_dim.html'])
start = time.time()
while time.time() - start < 5 and data is None:
    s.handle_request()
p.kill()
print('DIMENSIONS:', data)
