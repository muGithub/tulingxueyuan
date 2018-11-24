# encoding = utf-8
import threading
import time

#Python2
# from Queue mimport Queue

# Python
import queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 600:
                for i in range(100):
                    count = count + 1
                    msg = 'print' + str (count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = self.name + 'xiaofei' +queue.get()
                    print(msg)

            time.sleep(1)

if __name__ == '__main__':
    queue = queue.Queue()

    for i in range(500):
        queue.put("init"+str(i))

    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()

