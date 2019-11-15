class Parent(object):
    def __init__(self, name, *ags, **kwargs):
        print("parent init starting...")
        self.name = name
        print("parent init end...")


class Son1(Parent):
    def __init__(self, name, age, *ags, **kwargs):
        print("Son1 init starting...")
        self.age = age
        super().__init__(name, *ags, **kwargs)
        print("Son1 init end...")


class Son2(Parent):
    def __init__(self, name, gender, *ags, **kwargs):
        print("Son2 init starting...")
        self.gender = gender
        super().__init__(name, *ags, **kwargs)
        print("Son2 init end...")


class Grandson(Son1, Son2):
    def __init__(self, name, gender, age):
        print("Grandson init starting...")
        self.name = name
        self.gender = gender
        # super().__init__(name,gender,age)  #不带参 super 根据 mro 链查找继承关系
        # super(Grandson, self).__init__(name, gender, age)  # 带参则根据参数在 mro 中寻找 grandson 后一个
        super(Son2,self).__init__(name,gender,age) # 指名从 Son2 开始，只会调用 Parent
        print("Grandson init end...")


def main():
    print(Grandson.__mro__)  # 类似 js 原型连
    # (<class '__main__.Grandson'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class '__main__.Parent'>, <class 'object'>)

    grandson = Grandson("xxoo", "male", 18)


if __name__ == '__main__':
    main()
