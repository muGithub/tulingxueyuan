# 包含一个学生类
# 一个sayhello函数
# 一个打印语句

class Student():
    def __init__(self, name="Nonone", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))

def sayHello():
    print("Hi, welcome to here")


# 此判断语句建议一直作为程序的入口
if __name__ == '__main__':
    print("I'm mokuai 1")