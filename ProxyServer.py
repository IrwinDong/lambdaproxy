from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from urllib import parse
import queue

requestsqueue = queue.Queue()

url = 'https://www.google.com'

class HTTPRedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        requestsqueue.put_nowait(self.path)
        self.send_response(301)
        self.send_header('Location', url+self.path)
        self.end_headers()
        
    def do_POST(self):
        self.send_response(301)
        self.send_header('Location', url+self.path)
        self.end_headers()

    def do_HEAD(self):
        self.send_response(301)
        self.send_header('Location', url+self.path)
        self.end_headers()

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

def run(server_class=ThreadingMixIn, handler_class=HTTPRedirectHandler):
    server = ThreadingSimpleServer(('0.0.0.0', 8000), HTTPRedirectHandler)
    server.serve_forever()

if __name__ == '__main__':
    run()
