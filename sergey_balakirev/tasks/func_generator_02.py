"""
Мы с вами в заданиях несколько раз генерировали
последовательность чисел Фибоначчи,
которая строится по правилу: каждое последующее
число равно сумме двух предыдущих.
Для разнообразия давайте будем генерировать каждое
последующее как сумму трех предыдущих чисел.
При этом первые три числа равны 1 и имеем такую
последовательность:

1, 1, 1, 3, 5, 9, 17, 31, 57, ...

Не знаю, есть ли у нее название, поэтому, в рамках уроков,
я скромно назову ее последовательностью Балакирева.

Итак, на вход программы поступает натуральное
число N (N > 5) и необходимо определить функцию-генератор,
которая бы возвращала N первых чисел последовательности
Балакирева (включая первые три единицы).

Реализуйте эту функцию без использования коллекций
(списков, кортежей, словарей и т.п.).
Вызовите ее N раз для получения N чисел и выведите
полученные числа на экран в одну строчку через пробел.
"""


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


# fib(1000)

n = int(input())


def tribonachi(n):
    a, b, c = 1, 1, 1
    for i in range(n):
        yield a
        a, b, c, = b, c, a + b + c


res = tribonachi(n)

for i in res:
    print(i, end=" ")