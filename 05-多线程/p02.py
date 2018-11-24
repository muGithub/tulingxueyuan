'''
利用time函数，生成两个函数
顺序调用
计算机总的运行时间
'''

import time
import _thread as thread
def loop1():
    print('Strat loop1 at:', time.ctime())
    time.sleep(4)
    print("end loop1 ", time.ctime())

def loop2():
    print('Strat loop2 at:', time.ctime())
    time.sleep(2)
    print("end loop2 ", time.ctime())

def main():
    print("Strating at:", time.ctime())
    # 多线程执行函数
    # 启动多线程函数为start_new_thread
    thread.start_new_thread(loop1, ())
    thread.start_new_thread(loop2, ())
    print("ALL end:", time.ctime())

main()
