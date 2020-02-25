from queue import Queue
from LambdaProxyServer import LambdaRedirectHandler, LambdaProxyServer
from QueueManagerWorker import QueueManagerWorker
from PingConfig import PingConfig
import distributor

api_url = 'https://4gssmngr4e.execute-api.us-east-1.amazonaws.com/default/pack-tensorflow-dev-main'
queuemanager : QueueManagerWorker = None

def run():
    requestqueue = Queue()
    distributor.Instance = distributor.Distributor(requestqueue)
    config = PingConfig()
    config.RequestPath = api_url + '?ping=True'
    config.PingInterval = 300
    queuemanager = QueueManagerWorker(api_url, requestqueue, config)
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
