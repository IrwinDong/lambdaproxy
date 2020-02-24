class QueueManagerWorker:

    requestqueue = None

    def __init__(self, queue):
        self.requestqueue = queue