## python advance


#### tcp

tcp server必须绑定，而 client 最好不绑定，以防端口占用。
tcp client 连接 server 时，server 会创建新的 socket 并标记该 client 信息

#### udp

#### Threading

创建线程完成多任务，内存消耗小。
多线程执行顺序不定，由操作系统决定。
多线程共享全局变量。
互斥锁：
```python
locker = treading.Lock()
...

locker.acquire() # 判断是否在执行，执行中则锁住
...
locker.relase()  # 解锁
```
死锁

#### process
multiprocessing
多进程内存消耗大，效率低。
多进程不会共享全局变量。
多线程队列
多进程进程池： 主进程不等待     pool.join()


### 迭代器 生成器 

#### iterator
自定义迭代器，类中添加两个方法：
```python
# 创建可迭代方法
    def __iter__(self):
        return self

    # 创建迭代next 方法
    def __next__(self):
        if self.current_num < len(self.names):
            result = self.names[self.current_num]
            self.current_num += 1
            return result
        else:
            raise StopIteration  # 自定义异常 越界抛出

```
自定义迭代器可以大量节省空间。

#### generator
yield  生成器 是特殊的迭代器
协程实现并发 通过 yield 实现，消耗资源最小。
gevent 代替 yield 处理搞并发

