import time
import threading
def loop3(in1):
    print('Strat loop1 a1t: {0}',in1, time.ctime())
    time.sleep(4)
    print("end loop1 ", time.ctime())

def loop4(in1, in2):
    print('Strat loop2 at',in1, in2)
    time.sleep(2)
    print("end loop1 ", time.ctime())


def main():
    print("Starting at:", time.ctime())

    t1 = threading.Thread(target=loop3, args=('niui',))
    t1.start()

    t2 = threading.Thread(target=loop4, args=('****', 'dadf'))
    t2.start()

    print("ALL end:", time.ctime())

main()
while(1):
    pass