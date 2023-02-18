"""
Определите функцию-генератор,
которая бы возвращала простые числа.
(Простое число - это натуральное число,
которое делится только на себя и на 1).
Выведите с помощью этой функции первые 20 простых чисел
(начиная с 2) в одну строчку через пробел.
"""


def gen():
    num = 2
    while True:
        if is_prost(num):
            yield num
        num += 1


def is_prost(x):
    d = x - 1
    if d < 0:
        return False
    while d > 1:
        if x % d == 0:
            return False
        d -= 1
    return True


prost = gen()

for i in range(20):
    print(next(prost), end=" ")



# lst_prost = [x for x in range(20) if is_prost(x)]
# print(lst_prost)