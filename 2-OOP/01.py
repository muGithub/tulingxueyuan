'''
定义十个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass

#定义一个对象
xiawenjuan = Student()

# 定义一个空类
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    couse = "Python"


    # 注意
    # 1.def doHomework的缩进层级
    # 2.系统默认有一个self参数
    def doHomework(self):
        print("I've done")

        # 在函数末尾，推荐使用return 语句
        return None

# 实例化一个xiawen的学生，是一个具体的人
xiawen = PythonStudent()
print(xiawen.name)
print (xiawen.age)
# 注意成员函数的调用没有传递进入参数
xiawen.doHomework()