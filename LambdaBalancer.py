import queue
from LambdaProxyServer import LambdaRedirectHandler, LambdaProxyServer
import distributor

url = 'https://4gssmngr4e.execute-api.us-east-1.amazonaws.com/default/pack-tensorflow-dev-main'

def run():
    distributor.Instance = distributor.Distributor(url)
    server = LambdaProxyServer(('0.0.0.0', 8000), LambdaRedirectHandler)
    server.serve_forever()

if __name__ == '__main__':
    run()
