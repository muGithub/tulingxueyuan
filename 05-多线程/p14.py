# encoding = utf-8
import threading
import time

#Python2
# from Queue mimport Queue

# Python
import queue

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def func_1():
    print("func1")
    lock_1.acquire()
    print("申请1")
    time.sleep(2)
    lock_2.acquire()
    print("申请2")

    lock_2.release()
    print("释放2")
    lock_1.release()
    print("释放1")
    print("done 1")

def func_2():
    print("func2")
    lock_2.acquire()
    print("申请2")
    time.sleep(4)
    lock_1.acquire()
    print("申请1")

    lock_1.release()
    print("释放1")
    lock_2.release()
    print("释放2")
    print("done2")


if __name__ == '__main__':
    print("主程序")

    t1 = threading.Thread(target=func_1, args=())
    t2 = threading.Thread(target=func_2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()