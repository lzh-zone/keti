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

s = HTTPServer(('127.0.0.1', 8891), H)

p = subprocess.Popen([
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "--headless=new",
    "--disable-gpu",
    "--window-size=375,1000",
    "http://127.0.0.1:8891/debug_dim.html"
])
start = time.time()
while time.time() - start < 5 and data is None:
    s.handle_request()
p.kill()
print('DIMENSIONS WITH HEADLESS=NEW:', data)
