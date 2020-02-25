import urllib.request
from threading import Thread
import datetime

url = 'http://localhost:8000/?imagelink=http://images4.fanpop.com/image/photos/16700000/Dogs-dogs-16762058-1024-768.jpg'

def ping():
    with urllib.request.urlopen(url) as response:
        print(str(datetime.datetime.now()) + str(response.read()))


for i in range(100):
    thread = Thread(target=ping)
    thread.start()
