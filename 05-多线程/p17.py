import threading
import time

def  func():
    print("I'm running........")
    time.sleep(4)
    print("I'm done..........")

if __name__ == "__main__":
    t = threading.Timer(6, func)
    t.start()

    i = 0
    while True:
        print("{0}*************".format(i))
        time.sleep(2)
        i += 1