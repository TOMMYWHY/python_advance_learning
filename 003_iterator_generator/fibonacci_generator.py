def fibonacci(n):
    a, b = 0, 1
    current = 0
    while current < n:
        yield a  # 迭代时， 重复从此向下执行
        a, b = b, a + b
        current += 1


if __name__ == '__main__':
    obj = fibonacci(10)

    ret = next(obj)  # 生成器对象
    print(ret, end=" ")

    print()
    print("-------------")

    for item in obj:
        print(item, end=" ")
