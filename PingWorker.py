import threading
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
        id = threading.get_ident()
        while self.event.wait():
            print('ping start({}) {}'.format(id, datetime.now()))
            with urllib.request.urlopen(self.config.RequestPath):
                print('ping responded({}) {}'.format(id, datetime.now()))

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
    