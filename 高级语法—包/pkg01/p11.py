# 包含一个学生类
# 一个sayhello函数
# 一个打印语句

class student():
    def __init__(self, name = "noname", age = 18):
        self.name = name
        self.age = age

    def say(self):
        print("my name is {0}".format(self.name))

def SayHello():
    print("Hi,welcome to DaLian")

# 此判断语句，建议一直作为程序的入口
if __name__ == '__main__':
    print("你调用了p01")