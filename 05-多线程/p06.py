import time
import threading

def fun():
    print("fun")
    time.sleep(2)
    print("end fun")

print("Main ")

t1 = threading.Thread(target=fun, args=())

t1.setDaemon(True)

t1.start()

time.sleep(1)

print("Main")