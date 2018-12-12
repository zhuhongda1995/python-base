# 定义一个空的类
class Student():
    pass
# 定义一个对象
mingyue = Student()

#在定义一个类，用来描述听Python的
class PythonStudent():
    name = None
    age = 8
    course = "Python"

    # 需要注意
    # 1. 缩进层级
    # 2. 系统默认self参数
    def doHomework(self):
        print("I 在做作业")

        return None
yueyue = PythonStudent()
print(yueyue.course)
print(yueyue.age)
print(yueyue.name)
yueyue.doHomework()