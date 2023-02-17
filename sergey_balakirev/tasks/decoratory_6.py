"""

Вводится строка целых чисел через пробел. Напишите функцию, которая преобразовывает эту строку в список чисел и возвращает их сумму.

Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для введенной строки s:

s = input()

Результат отобразите на экране.
"""


def decorator(start=5):
    def decor(func):
        return lambda *args, **kwargs: func(*args, **kwargs) + start
    return decor


@decorator(start=5)
def string_to_int(text):
    return sum(list(map(int, text.split())))


def main():
    print(string_to_int(input()))


if __name__ == '__main__':
    main()
