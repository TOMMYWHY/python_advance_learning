from pymysql import connect


class Shop(object):
    def __init__(self):
        self.conn = connect(host="localhost", port=3306, user="root", password="12345678", database="point_of_sales",
                            charset="utf8")
        self.cursor = self.conn.cursor()

    def __delete__(self, instance):
        self.cursor.close()
        self.conn.close()

    def show_all_products(self):
        sql = "select * from products;"
        self.execute_sql(sql)

    def show_all_tasks(self):
        sql = "select * from tasks;"
        self.execute_sql(sql)

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    @staticmethod  # 静态方法
    def print_menu():
        print("----shopping----")
        print("1. all products")
        print("2. all task")
        return input("enter number: ")

    def run(self):
        while True:
            num = self.print_menu()
            if num == "1":
                self.show_all_products()
            elif num == "2":
                self.show_all_tasks()
            else:
                print("enter number:")


def main():
    shop = Shop()
    shop.run()


if __name__ == '__main__':
    main()
