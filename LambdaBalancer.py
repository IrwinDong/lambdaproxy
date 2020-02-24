import queue
from LambdaServer import LambdaRedirectHandler, ThreadingSimpleServer

requestsqueue = queue.Queue()

url = 'https://4gssmngr4e.execute-api.us-east-1.amazonaws.com/default/pack-tensorflow-dev-main'

def run():
    server = ThreadingSimpleServer(('0.0.0.0', 8000), LambdaRedirectHandler)
    server.serve_forever()

if __name__ == '__main__':
    run()
