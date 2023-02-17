"""Алгоритм Евклида"""
import time


def get_nod(a, b):
    """
    Вычисляется НОД для натуральных чисел a и b по
    алгоритму Евклида(медленный).
    :param a: Первое натуральное число
    :param b: Второе натуральное число
    :return: НОД
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def get_nod_fast(a, b):
    """
    Вычисляется НОД для натуральных чисел a и b по
    алгоритму Евклида(быстрый).
    :param a: Первое натуральное число
    :param b: Второе натуральное число
    :return: НОД
    """
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


# res = get_nod(18, 24)
# print(res)
# help(get_nod)


def test_nod(func):
    # --------- test 1 -----------
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print("#test1 -- ok")
    else:
        print("#test1 -- fail")

    # --------- test 2 -----------
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print("#test2 -- ok")
    else:
        print("#test2 -- fail")

    # --------- test 2 -----------
    a = 2
    b = 10000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 0.5:
        print("#test3 -- ok")
    else:
        print("#test3 -- fail")


for i in range(10):
    test_nod(get_nod)

print("=" * 50)

for i in range(10):
    test_nod(get_nod_fast)