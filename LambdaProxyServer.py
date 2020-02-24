from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import distributor

class LambdaRedirectHandler(BaseHTTPRequestHandler):
   
    def do_GET(self):
        distributor.Instance.distribute(self.path, self)
        
    def do_POST(self):
        distributor.Instance.distribute(self.path, self)

    def do_HEAD(self):
        distributor.Instance.distribute(self.path, self)

class LambdaProxyServer(ThreadingMixIn, HTTPServer):
    pass