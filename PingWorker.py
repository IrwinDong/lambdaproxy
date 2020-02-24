from threading import Thread, Timer
from PingConfig import PingConfig
import urllib

class PingWorker:
    config:PingConfig
    timer = None

    def __init__(self, config):
        self.config = config

    def ping(self):
        for i in range(self.config.PingWorker):
            urllib.request.Request(self.config.url)

    def runasync(self):
        self.timer = Timer(self.config.PingInterval, self.ping)
        self.timer.daemon = True
        self.timer.start()



    