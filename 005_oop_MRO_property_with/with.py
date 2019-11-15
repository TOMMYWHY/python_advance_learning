# context 上下文管理器
class File(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("entering...")
        self.f = open(self.filename, self.mode)
        return self.f

    # def __exit__(self, exc_type, exc_val, exc_tb):
    def __exit__(self, *args):
        print("exiting....")
        self.f.close()


def main():
    with File('out.txt', 'w') as f:
        print('writing...')
        print(f)
        f.write("testing....") 


if __name__ == '__main__':
    main()
