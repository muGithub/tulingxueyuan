import  threading
import time

# 1.需要继承子threading.Thread
class MyThread(threading.Thread):
    def __init__(self, arg):
        super(MyThread, self).__init__()
        self.arg = arg

    # 2.必须重写run函数，run函数掉膘的是真正执行的功能
    def run(self):
        time.sleep(2)
        print("the args is {0}".format(self.arg))

for i in range(5):
    t = MyThread(i)
    t.start()
    t.join()


print("Main thread is done")