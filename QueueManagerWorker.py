from threading import Thread
from queue import Queue
from distributor import LambdaRequest
import distributor
from PingConfig import PingConfig
from PingWorker import PingWorker

class QueueManagerWorker:
    targeturl:str = None
    queue : Queue = None
    config : PingConfig
    thread:Thread = None
    stopping = False
    pingworker = None


    def __init__(self, targeturl:str, queue:Queue, config:PingConfig):
        self.targeturl = targeturl
        self.queue = queue
        self.config = config
        self.pingworker = PingWorker(self.config)

    def processqueue(self):
        while not self.stopping:
            request: LambdaRequest = self.queue.get(True)
            request.url = self.targeturl+request.path
            request.waithandler.set()

    def runasync(self):
        self.thread = Thread(target=self.processqueue, daemon=True)
        self.thread.start()
        self.pingworker.runasync()

    def stop(self):
        self.stopping = True
    
