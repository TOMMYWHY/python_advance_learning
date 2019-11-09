class Team(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

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


def main():
    team = Team()
    team.add("tommy")
    team.add("sookie")
    team.add("testing")

    for name in team:
        print(name)


if __name__ == '__main__':
    main()
