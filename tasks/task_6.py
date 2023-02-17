"""Высокосный год"""


class Year:

    def __init__(self, year):
        self.__year = year

    def verify_year(self):
        if not isinstance(self.__year, int):
            raise TypeError("Число должно быть int")
        if not (1900 <= self.__year <= 3000):
            raise TypeError("Число должно быть в диапазоне от 1900 до 3000")
        return True

    def leap_year(self):
        if self.verify_year():
            if (self.__year % 4 == 0 and self.__year % 100 != 0) or self.__year % 400 == 0:
                print("Високосный")
            else:
                print("Обычный")


year = int(input())
y = Year(year)
y.leap_year()

