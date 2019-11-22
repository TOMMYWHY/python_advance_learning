# 通过闭包形式 为函数前 后 添加功能
# 相当于 将 test1 的引用 重新指向 set_fun1 内 定义的函数 call_func

def set_fun1(func):
    print("preparing..")  # py 解释器 上来就执行装饰器
    def call_func():
        print("decorator.....")
        func()
    return call_func

@ set_fun1
def test1():
    print("test1.... ")



def set_fun2(func):
    def call_func(n):
        print("decorator.....")
        func(n)
    return call_func

@ set_fun2
def test2(num):
    print("test1.... %d" % num)


# ret = set_fun(test1)


# 通用装饰器
def set_fun3(func):
    def call_func(*args,**kwargs):
        print("decorator.....")
        return func(*args,**kwargs)
    return call_func


def main():
    test1()
    test2(100)
if __name__ == '__main__':
    main()
