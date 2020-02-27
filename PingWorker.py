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
        while self.event.wait():
            print('ping start ' + str(datetime.now()))
            with urllib.request.urlopen(self.config.RequestPath) as response:
                print('ping ' + str(datetime.now()) + str(response.read()))

    def ping(self):
        for i in range(self.config.PingWorker):
            thread = Thread(target=self.poke)
            thread.daemon = True
            thread.start()
        while not self.event.wait(self.config.PingInterval):
            self.event.set()
            self.event.clear()


    def runasync(self):
        thread = Thread(target=self.ping)
        thread.daemon = True
        thread.start()
    