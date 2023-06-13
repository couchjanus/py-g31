from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import cgi

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def server_close(self):
        self.socket.close()
        
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        if self.path == '/form':
            self.path = '/form.html' 
        try:
            sendReply = False
            if self.path.endswith('.html'):
                mimetype = 'text/html'
                sendReply = True
            if sendReply == True:
                f = open(curdir + sep + self.path, 'rb')
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return
        except IOError:
            self.send_error(404, f'File Not Found: {self.path}')
            
    def do_POST(self):
        if self.path == '/send':
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST',
                             'CONTENT_TYPE':self.headers['Content-Type']})
            res = form['your_name'].value
                
            print(f"Yiur name : {res}")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Thanks %s !' % res.encode('utf-8'))
            return


if __name__ == "__main__":
    httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler) 
    print(F"Started http server on port 8000")
    httpd.serve_forever()

