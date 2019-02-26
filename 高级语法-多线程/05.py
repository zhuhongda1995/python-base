'''
利用time函数，生成两个函数
利用多线程调用
计算总的运行时间
练习带参数的多线程启动方法
'''

import time
import threading

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
    # 生成threading.Thread实例
    t1 = threading.Thread(target=loop1, args=("王大天",))
    t1.start()

    t2 = threading.Thread(target=loop2, args=("王大天", "王大地"))
    t2.start()

    t1.join()
    t2.join()
    print('All done at :', time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)