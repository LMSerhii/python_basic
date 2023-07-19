class Person:

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

    # old = property(get_old, set_old)


p = Person('Serhii', 20)
print("=" * 20)
# del p.old
p.old = 34
print(p.__dict__)
# print(Person.__dict__)



