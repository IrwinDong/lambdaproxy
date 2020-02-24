from http.server import BaseHTTPRequestHandler
from queue import Queue, Full

class LambdaRequest:
    path = None
    handler : BaseHTTPRequestHandler = None
    
    def __init__(self, path:str, handler:BaseHTTPRequestHandler):
        self.path = path
        self.handler = handler
        
class Distributor:
    requestqueue = Queue()
    targeturl : str

    def __init__(self, targeturl:str):
        self.targeturl = targeturl

    def distribute(self, path:str, handler:BaseHTTPRequestHandler):
        request = LambdaRequest(path, handler)
        try:
            self.requestqueue.put(request, True, 5)
        except Full:
            handler.send_error(504, "server is busy")
        handler.send_response(301)
        handler.send_header('Location', self.targeturl+path)
        handler.end_headers()

Instance:Distributor = None