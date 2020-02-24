from threading import Thread
from queue import Queue
from distributor import LambdaRequest
import distributor

class QueueManagerWorker:
    targeturl:str = None
    queue : Queue = None

    def __init__(self, targeturl:str, queue:Queue):
        self.targeturl = targeturl
        self.queue = queue

    def processqueue(self):
        while True:
            request: LambdaRequest = self.queue.get(True)
            request.url = self.targeturl+request.path
            request.waithandler.set()

    def runasync(self):
        thread = Thread(target=self.processqueue)
        thread.start()
    
