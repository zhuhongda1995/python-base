'''
利用time函数，生成两个函数
利用多线程调用
计算总的运行时间
练习带参数的多线程启动方法
'''

import time
import _thread as thread

def loop1(in1):
    # ctime 得到当前时间
    print('Start loop1 at :', time.ctime())
    # 打印参数
    print("我是参数", in1)
    time.sleep(4)
    print('End loop1 at :', time.ctime())
def loop2(in1, in2):
    # ctime 得到当前时间
    print('Start loop1 at :', time.ctime())
    # 打印参数
    print("我是参数", in1, "和参数", in2)
    time.sleep(2)
    print('End loop2 at :', time.ctime())


def main():
    print('Start at :', time.ctime())
    # 启用多线程的意思是用多线程去执行某个函数
    # 启用多线程函数为start_new_thread
    # 参数两个，一个是需要运行的函数名，第二个是函数的参数作为元祖使用，为空则是空元祖
    # 注意，如果函数只有一个参数，需要参数后有一个逗号
    thread.start_new_thread(loop1, ("王大天",))
    thread.start_new_thread(loop2, ("王大地", "王大锤"))
    print('All done at :', time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)