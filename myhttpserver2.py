from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

PORT = 9999

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        qindex = self.path.find('?')
        if qindex == -1:
            req_url = self.path[:len(self.path)]
        else:
            req_url = self.path[:qindex]

        if req_url != '/graph':
            self.send_error(404, 'FileNot Found')
            return

        handler_name = 'ex' + self.get_parameter('ex')
        if handler_name not in MyHTTPRequestHandler.__dict__:
            self.send_error(404, 'FileNot Found')
            return

        MyHTTPRequestHandler.__dict__[handler_name](self)


    def get_parameter(self, name):
        qindex = self.path.find('?')

        qs = '' if qindex == -1 else self.path[qindex+1:]

        params = parse_qs(qs)
        values = params.get(name)

        return None if values is None else values.pop()

    def ex1(self):
        self.send_response(200)
        self.send_header('Content-Type, ', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write('<h1>Hello World</h1>'.encode('utf-8'))

    def ex2(self):
        arr = np.random.normal(5, 3, 500)
        fig, subplots = plt.subplots(2, 1)
        subplots[0].plot(arr, color='red', linestyle='solid')
        subplots[1].hist(arr, bins=20, edgecolor='black', linewidth=1.2)

        buffer = BytesIO()
        plt.savefig(buffer, dpi=80, bbox_inches='tight')
        plt.clf()

        self.send_response(200)
        self.send_header('Content-Type, ', 'image/png')
        self.end_headers()
        self.wfile.write(buffer.getvalue())


# 서버구동
httpd = HTTPServer(('', PORT), MyHTTPRequestHandler)
print('HTTP Server Runs on Port(%d)'% (PORT))
httpd.serve_forever()