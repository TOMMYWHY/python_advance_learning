# 与 js 闭包含义一致。
# 一个函数 将 私有变量 返回出去。


def line(k, b):
    def create_y(x):
        print(k * x + b)  # 将封闭的形参 k b 返回出去

    return create_y


def main():
    l = line(1, 2)
    l(0)
    l(1)
    l(2)


if __name__ == '__main__':
    main()
