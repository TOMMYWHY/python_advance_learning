class Goods:
    @property
    def price(self):
        print("getting price")

    @price.setter
    def price(self, value):
        print("setting price")


class Goods2:
    def __init__(self):
        self.__price = 0

    def get_price(self):
        print("getter")
        return self.__price

    def set_price(self, value):
        print("setter")
        self.__price = value

    price = property(get_price, set_price)


def main():
    good = Goods()
    good.price
    good.price = 100
    print("=========")

    good2 = Goods2()
    good2.price = 2000
    print(good2.price)

if __name__ == '__main__':
    main()
