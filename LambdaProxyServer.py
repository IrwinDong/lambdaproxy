from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import distributor
import threading

class LambdaRedirectHandler(BaseHTTPRequestHandler):
   
    def do_GET(self):  
        self.handlerequest()
        
    def do_POST(self):
        self.handlerequest()

    def do_HEAD(self):
        self.handlerequest()

    def handlerequest(self):
        (timeout, url) = distributor.Instance.distribute(self.path)
        if(timeout):
            self.send_error(504, "proxy server timeout")
        else:
            self.send_response(302)
            self.send_header('Location', url)
            self.end_headers()


class LambdaProxyServer(ThreadingMixIn, HTTPServer):
    pass