from string import ascii_letters


class Person:

    S_UKR = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
    S_UKR_UPPER = S_UKR.upper()

    def __init__(self, fio, age, ps, weight):

        # self.verify_fio(fio)
        # self.verify_age(age)
        # self.verify_ps(ps)
        # self.verify_weight(weight)
        #
        # self.__fio = fio.split()
        # self.__age = age
        # self.__ps = ps
        # self.__weight = weight

        self.fio = fio
        self.age = age
        self.ps = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ПІБ повинно бути строкою")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Невірний формат ПІБ")

        letters = ascii_letters + cls.S_UKR + cls.S_UKR_UPPER

        for s in f:
            if len(s) < 1:
                raise TypeError("В ПІБ повинен бути хоча б один символ")
            if len(s.strip(letters)) != 0:
                raise TypeError("В ПІБ можна використовувати тільки літери та дефіс")

    @classmethod
    def verify_age(cls, age):
        if type(age) != int or age < 14 or age > 65:
            raise TypeError("Вік повинен бути цілим числом в діапазоні [14; 100]")

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError("Вага повинна бути дійсним числом від 20 і вище")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Паспорт повинен бути строкою")
        s = ps.split()
        if len(s) != 2 or len(s[0]) != 2 or len(s[1]) != 6:
            raise TypeError("Невірний формат паспорту")

        for i in s[1]:
            if not i.isdigit():
                raise TypeError("Номер паспорту повинен бути числом")

        for i in s[0]:
            if not i.isalpha():
                raise TypeError("Серія повинная бути із літер")
            if not i.isupper():
                raise TypeError("Серія повинная бути із літер в верхньому регістрі")

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def ps(self):
        return self.__ps

    @ps.setter
    def ps(self, ps):
        self.verify_ps(ps)
        self.__ps = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight


p = Person("Леонов Сергій Миколайович", 33, "MN 270131", 133.5)

p.fio = "Балакирев Ростислав Петрович"
p.age = 45
p.ps = "SR 656984"
p.weight = 122.2
print(p.__dict__)