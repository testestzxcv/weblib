from http.server import BaseHTTPRequestHandler, HTTPServer

port = 9999
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type, ', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write('<h1>Hello World</h1>'.encode('utf-8'))

# 서버구동
httpd = HTTPServer(('', 9999), MyHTTPRequestHandler)
print('HTTP Server Starts....')
httpd.serve_forever()   # 무한루프로 돌아라