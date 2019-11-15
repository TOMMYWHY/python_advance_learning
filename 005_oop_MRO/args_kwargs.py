def test2(a, b, *args, **kwargs):
    print("****************")
    print(a)
    print(b)
    print(args)
    print(kwargs)


def test1(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    test2(a, b, args, kwargs)  # ((33, 44, 55), {'name': 'wocao', 'age': 18}) 所有益处参数都被元组
    test2(a, b, *args, *kwargs) # (33, 44, 55, 'name', 'age') 加*被拆
    test2(a, b, *args, **kwargs) # (33, 44, 55) {'name': 'wocao', 'age': 18}



def main():
    test1(1, 2, 33, 44, 55, name="wocao", age=18)


if __name__ == '__main__':
    main()
