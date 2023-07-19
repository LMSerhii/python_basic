from datetime import datetime


class Goods:

    def __init__(self, name, weight, price):
        super().__init__()
        print("__init__Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def get_info(self):
        print(f"{self.name} {self.weight} {self.price}")


class Mixinlog:
    ID = 0

    def __init__(self):
        print("__init__ Mixinlog")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: Товар был продан в {datetime.now().strftime('%H:%M')} часов ")

    def get_info(self):
        print("get_info in Mixinlog")


class NoteBook(Goods, Mixinlog):
    def get_info(self):
        Mixinlog.get_info(self)


n = NoteBook('Asus', 1.5, 55000)
n.get_info()
n.save_sell_log()
print(NoteBook.__mro__)
