from queue import Queue, Full
from threading import Event
from datetime import datetime

class LambdaRequest:
    path = None
    waithandler : Event = None
    url : str = None
    timeout : bool = False
    arrival : datetime = datetime.max
    depature : datetime = datetime.min
    
    def __init__(self, path:str, waithandler:Event):
        self.path = path
        self.waithandler = waithandler
        self.arrival = datetime.now()

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
            else:
                request.depature = datetime.now()
        return request.timeout, request.url, request.depature-request.arrival

Instance:Distributor = None