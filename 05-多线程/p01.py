'''
利用time函数，生成两个函数
顺序调用
计算机总的运行时间
'''

import time

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
    loop1()
    loop2()
    print("ALL end:", time.ctime())

if __name__ == '__main()__':
    main()