#! /usr/bin/python
from http.server import HTTPServer, BaseHTTPRequestHandler

accept_ip = '127.0.0.1'
accept_port = 8080

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


httpd = HTTPServer((accept_ip, accept_port), Serv)
httpd.serve_forever()