from queue import Queue
from LambdaProxyServer import LambdaRedirectHandler, LambdaProxyServer
import distributor
from QueueManagerWorker import QueueManagerWorker
from PingConfig import PingConfig

url = 'https://4gssmngr4e.execute-api.us-east-1.amazonaws.com/default/pack-tensorflow-dev-main'
queuemanager : QueueManagerWorker = None

def run():
    requestqueue = Queue()
    distributor.Instance = distributor.Distributor(requestqueue)
    config = PingConfig()
    config.RequestPath = 'https://4gssmngr4e.execute-api.us-east-1.amazonaws.com/default/pack-tensorflow-dev-main?ping=True'
    config.PingInterval = 300
    queuemanager = QueueManagerWorker(url, requestqueue, config)
    queuemanager.runasync()
    server = LambdaProxyServer(('0.0.0.0', 8000), LambdaRedirectHandler)
    server.serve_forever()

def cleanwork():
    if queuemanager is not None:
        queuemanager.stop()

import atexit
if __name__ == '__main__':
    atexit.register(cleanwork)
    run()
