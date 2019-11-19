## 问：说说Python多线程与多进程的区别?

## 答：

1. 多线程可以共享全局变量，多进程不能

2. 多线程中，所有子线程的进程号相同；多进程中，不同的子进程进程号不同

3. 线程共享内存空间；进程的内存是独立的

4. 同一个进程的线程之间可以直接交流；两个进程想通信，必须通过一个中间代理来实现

5. 创建新线程很简单；创建新进程需要对其父进程进行一次克隆

6. 一个线程可以控制和操作同一进程里的其他线程；但是进程只能操作子进程

两者最大的不同在于：在多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响；而多线程中，所有变量都由所有线程共享 。

### 具体介绍:
1. 多线程

在Python的标准库中提供了两个模块：`_thread`和`threading`，`_thread`是低级模块不支持守护线程，当主线程退出时，所有子线程都会被强行退出。而`threading`是高级模块，用于对`_thread`进行了封装支持守护线程。在大多数情况下我们只需要使用`threading`这个高级模块即可。

![image](https://mmbiz.qpic.cn/mmbiz_jpg/IibUVnJ665WoeahAAKiaXmTwNib9NrnibmiapzMTW1AbTSrlgcOQVVZFeXg8v1Z2kg6uiadhhVX34a4Q24DUzgzOgKCw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

> https://www.jianshu.com/p/6f14d1874f7f

2. 多进程

多进程是`multiprocessing`模块提供远程与本地的并发，在一个`multiprocessing`库的使用场景下，所有的子进程都是由一个父进程启动来的，这个父进程成为master进程，它会管理一系列的对象状态，一旦这个进程退出，子进程很可能处于一个不稳定的状态，所以这个父进程尽量要少做事来保持其稳定性 。

![image](https://mmbiz.qpic.cn/mmbiz_jpg/IibUVnJ665WoeahAAKiaXmTwNib9Nrnibmiap3D8icKsMVXC4Yqu4qsqRC8xOZAV49Tso7bQfpbyZmoE5BDKka7JqiaAg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

> https://www.jianshu.com/p/d648f160543b