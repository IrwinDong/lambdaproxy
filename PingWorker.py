from threading import Thread, Event
from PingConfig import PingConfig
import urllib.request
from datetime import datetime

class PingWorker:
    config:PingConfig
    event = None

    def __init__(self, config):
        self.config = config
        self.event = Event()

    def poke(self):
        with urllib.request.urlopen(self.config.RequestPath) as response:
            print('ping ' + str(datetime.now()) + str(response.read()))

    def ping(self):
        while not self.event.wait(self.config.PingInterval):
            for i in range(self.config.PingWorker):
                thread = Thread(target=self.poke)
                thread.daemon = True
                thread.start()

    def runasync(self):
        thread = Thread(target=self.ping)
        thread.daemon = True
        thread.start()
    