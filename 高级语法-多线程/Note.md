# 环境
- anaconda
- pycharm
- pyhton3.6
- http://www.cnblogs.com/jokerbj/p/7460260.html

# 多线程 vs 多进程
- 程序：一堆代码以文本的形式存入一个文档
- 进程：程序运行的一个状态
    - 包含地址空间、内存、数据栈等
    - 每个进程有自己完全独立的运行环境，多进程共享数据是一个问题
- 线程：一个进程的独立运行片段，一个进程可以有多个线程
    - 轻量化的进程
    - 一个进程的多个线程间共享数据和上下文运行环境
    - 共享互斥问题
- 全局解释器锁（GIL）
    - Python代码的之星石油python虚拟机进行控制
    - 在主循环中只能有一个控制线程在执行
- Python包
    - thread：有问题，不好用，Python3改成了_thread
    - threading：通行的包
    
    案例 01.py 顺序执行，耗时较长
    案例 02.py 该用多线程，缩短总时间，使用_thread
    案例 03.py 多线程传参数
    
- threading的使用
    - 直接利用threading.Thread生成Thread实例
        1.t = threading.Thread(target=xxx, args=(xxx,))
        2.t.start()：启动多线程
        3.t.join()：等待多线程执行完成
        
        案例04.py
        案例05.py：加入join后跟案例04.py比较
        - 守护线程：deamon
            - 如果在程序中将子线程设置成守护线程，则子线程在主线程结束时自动退出
            - 一般认为守护线程不重要或者不允许离开主线程独立运行
            - 守护线程案例能否有效跟环境有关
            
            案例06.py 非守护线程
            案例07.py 守护线程
        - 线程常用属性
            threading.currentThread：返回当前线程变量
            threading.enumerate:返回一个包含正在运行的线程的list，正在运行的线程指的是线程启动后，结束前的状态
            threading.activeCount: 返回正在运行的线程数量，效果跟 len(threading.enumerate)相同
            thr.setName: 给线程设置名字
            thr.getName: 得到线程的名字
    - 直接继承自threading.Thread
        - zhijiejicheng Thread
        - 重写run函数
        - 类实例可以直接运行
        
        案例 09.py
        案例 10.py 工业风案例