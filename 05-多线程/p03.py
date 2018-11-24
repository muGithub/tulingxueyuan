import time
import _thread as thread
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

    thread.start_new_thread(loop3, ('niui',))
    thread.start_new_thread(loop4, (1, 'dadf'))
    print("ALL end:", time.ctime())

main()