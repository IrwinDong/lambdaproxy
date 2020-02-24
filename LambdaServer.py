from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from urllib import parse

class LambdaRedirectHandler(BaseHTTPRequestHandler):
    requestqueue=None
    targeturl=''

    def __init__(self, targeturl, queue):
        self.requestqueue = queue
        self.targeturl = targeturl

    def do_GET(self):
        self.requestqueue.put_nowait(self.path)
        self.send_response(301)
        self.send_header('Location', self.targeturl+self.path)
        self.end_headers()
        
    def do_POST(self):
        self.send_response(301)
        self.send_header('Location', self.targeturl+self.path)
        self.end_headers()

    def do_HEAD(self):
        self.send_response(301)
        self.send_header('Location', self.targeturl+self.path)
        self.end_headers()

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass