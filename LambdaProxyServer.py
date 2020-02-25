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
        (timeout, url, servicetime) = distributor.Instance.distribute(self.path)
        if(timeout):
            self.send_error(504, "proxy server timeout")
            print('service timeout:' + self.path)
        else:
            self.send_response(302)
            self.send_header('Location', url)
            self.end_headers()
            print('service time:' + str(servicetime) + ':' + self.path)


class LambdaProxyServer(ThreadingMixIn, HTTPServer):
    pass