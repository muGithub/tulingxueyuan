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
    lock_1.acquire(timeout=4)
    print("1申请1")
    time.sleep(2)
    rst = lock_2.acquire(timeout=2)
    print("1申请2")

    if rst:
        print("fun1得到lock2")
        lock_2.release()
        print("1释放2")
    else:
        print("1没得到lock2")
    lock_1.release()
    print("1释放1")
    print("done 1")

def func_2():
    print("func2")
    lock_2.acquire(timeout=4)
    print("2申请2")
    time.sleep(4)
    rst = lock_1.acquire(timeout=2)
    print("2申请1")

    if rst:
        print("fun2得到lock1")
        lock_1.release()
        print("21释放1")
    else:
        print("2没得到lock1")


    lock_2.release()
    print("2释放2")
    print("done2")


if __name__ == '__main__':
    print("主程序")

    t1 = threading.Thread(target=func_1, args=())
    t2 = threading.Thread(target=func_2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()