# 环境
- xubuntu 16.04
- anaconda
- pycharm
- python3.6
- https://www.cnblogs.com/jokerbj/p/7460260.html
- https://www.dabeaz.com/python/UnderstandingGIL.pdf

# 多进程vs多线程
- 程序：一堆代码以文本形式存入一个文档
- 进程：程序运行的一个状态
    - 包含地址空间，内存，数据栈等
    - 每个进程有自己完全独立的运行环境，多进程共享数据是一个问题
- 线程
    - 一个进程的独立运行片段，一个进程可以有多个线程
    - 轻量化的进程
    - 一个进程的多个线程共享数据和上下文运行环境
    - 共享互斥问题
- 全局解释器锁
    - Python代码的执行是由Python虚拟机控制
    - 在主循环中只能有一个控制线程在执行
    - 


- Python包
    - thread：有问题不好用，Python3改成了_thread
    - threading:同行的包
- 示例p01：顺序执行，耗时较长
- 示例p02:改用多线程，缩短总时间
- 多线程，传参数

- threading的使用
    - 直接利用threading.Thread生成Thread的实例
    - 1. t = threading.Thread(target=xxx, args(xxx, ))
    - 2. t.start():启动多线程
    - 3. t.join():等待多线程执行完成
    - 4. 案例04
    - 5. 案例05，加入join（）与04结果的比较
    - 守护线程-daemon
        - 如果在程序中将子线程设置成守护线程，则子线程会在主线程结束的时候自动退出
        - 一般认为，守护线程不重要或者不允许离开主线程独立运行
        - 守护线程示例能否有效果跟环境相关
        - 非守护线程 05
        - 守护线程 06
        
    - 线程常用属性
        - threadinng.currentThread
        - thr.setName:
        - thr.getName:
        - threading.enumerate
        - htreading.activeCount
        
- 直接继承自threading.Thread
    - 直接继承Thread
    - 重写run函数
    - 类实例可以直接运行
    - 示例08
    - 示例10 工业风示例
    
- 共享变量
    - 共享变量：当多个线程同时访问同一个变量，会产生共享变量冲突的问题
    - 示例11
    - 解决变量：锁，信号灯
    - 锁（lock）
        - 是一个标志，表示一个线程在占用一些资源
        - 使用方法
            - 上锁
            - 使用共享资源，放心使用
            - 取消所，释放锁
        - 示例 12
        - 锁谁：哪个资源需要多个线程共享，锁哪个
        - 理解锁：锁相当于一个标志
    - 线程安全问题：
        - 如果一个资源/变量，它对于多线程来讲，不用枷锁也不会引起任何问题，则成为线程安全
        - 线程不安全变量类型：list，set, dict
        - 线程安全变量类型：queue
    - 生产消费者问题
        - 一个模型,可以用来搭建消息队列
        - queue是一个用来存放变量的的数据结构，特点是先进先出，内部元素排队，可以理解为一个特殊的list
    - 死锁问题，案例14
    - 所的等待时间问题，示例15
    - semphore
        - 允许一个资源最多可有几个线程使用
        - 示例16
        
    - threading.Timer
    - 示例17
    - Timer是利用多线程，在指定时间后启动一个功能
    
- 可重入锁
    - 一个锁，可以被一个线程多次申请
    - 主要解决递归调用的时候，需要申请锁的情况
    - 示例18
    
# 线程替代方案
- subprocess
    - 完全跳过线程，使用进程
    - 是派生进程的主要替代方案
    - Python2.4之后引入
- multiprocessing
    - 使用threading接口派生，使用子进程
    - 允许为多核或者多cpu派生进程，接口跟threading非常相似
    - Python2.6
    
- concurrent.futures
    - 新的异步执行模块
    - 任务级别的操作
    - Python3.2后引入
# 多进程
- 进程间通讯（InterprocessCommunication. IPC)
- 进程之间无任何共享状态
- 进程的创建
    - 直接生成Process实例对象
    - 示例p19
    - 派生子类，示例20
    
- 在os中查看pid，ppid以及他们的关系
    - 示例 21
- 生产者消费者模型
    - JoinableQueue
    - 示例22
    - 队列中哨兵的使用，示例23
    - 哨兵的改进，示例24