from queue import Queue
from LambdaProxyServer import LambdaRedirectHandler, LambdaProxyServer
import distributor
from QueueManagerWorker import QueueManagerWorker

url = 'https://4gssmngr4e.execute-api.us-east-1.amazonaws.com/default/pack-tensorflow-dev-main'

def run():
    requestqueue = Queue()
    distributor.Instance = distributor.Distributor(requestqueue)
    queuemanager = QueueManagerWorker(url, requestqueue)
    queuemanager.runasync()
    server = LambdaProxyServer(('0.0.0.0', 8000), LambdaRedirectHandler)
    server.serve_forever()

if __name__ == '__main__':
    run()
