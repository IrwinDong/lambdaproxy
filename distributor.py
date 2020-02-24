from queue import Queue, Full
from threading import Event

class LambdaRequest:
    path = None
    waithandler : Event = None
    url : str = None
    timeout : bool = False
    
    def __init__(self, path:str, waithandler:Event):
        self.path = path
        self.waithandler = waithandler

class Distributor:
    requestqueue = None

    def __init__(self, queue:Queue):
        self.requestqueue = queue

    def distribute(self, path:str,):
        waithandler = Event()
        request = LambdaRequest(path, waithandler)
        try:
            self.requestqueue.put(request, True, 5)
        except Full:
            request.timeout = True
        else:
            if not waithandler.wait(10):
                request.timeout = True
        return request.timeout, request.url

Instance:Distributor = None