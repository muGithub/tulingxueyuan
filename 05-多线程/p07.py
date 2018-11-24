import time
import threading
def loop3(in1):
    print('Strat loop1 a1t: {0}',in1, time.ctime())
    time.sleep(6)
    print("end loop1 ", time.ctime())

def loop4(in1, in2):
    print('Strat loop2 at',in1, in2)
    time.sleep(3)
    print("end loop2 ", time.ctime())

def loop5(in1, in2):
    print('Strat loop3 at',in1, in2)
    time.sleep(5)
    print("end loop3 ", time.ctime())

def main():
    print("Starting at:", time.ctime())

    t1 = threading.Thread(target=loop3, args=('niui',))
    t1.setName("T_1")
    t1.start()

    t2 = threading.Thread(target=loop4, args=('****', 'dadf'))
    t2.setName("T_2")
    t2.start()

    t3 = threading.Thread(target=loop5, args=('niui','552'))
    t3.setName("T_3")
    t3.start()

    time.sleep(2)

    for thr in threading.enumerate():
        print("正在运行： {0}".format(thr.getName()))
        print("正在子线程运行： {0}".format(threading.activeCount()))

    print("ALL end:", time.ctime())

main()
while(1):
    pass