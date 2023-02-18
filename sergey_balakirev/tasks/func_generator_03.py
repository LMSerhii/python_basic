"""

Вводится натуральное число N (N > 8).
Необходимо определить функцию-генератор,
которая бы выдавала пароль длиной N символов из случайных букв,
цифр и некоторых других знаков.
Для получения последовательности допустимых символов для
генерации паролей в программе импортированы две строки:
ascii_lowercase, ascii_uppercase (см. листинг ниже),
на основе которых формируется общий список:

from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
Функция-генератор должна при каждом вызове возвращать новый
пароль из случайно выбранных символов chars длиной N и
делать это бесконечно, то есть, вызывать ее можно
бесконечное число раз. Сгенерировать случайный
индекс indx в диапазоне [a; b] для символа можно с
помощью функции randint модуля random:

import random
random.seed(1)
indx = random.randint(a, b)
Сгенерируйте с помощью этой функции первые пять
паролей и выведите их в столбик (каждый с новой строки).
"""

import random
from string import ascii_lowercase, ascii_uppercase

n = 8

chars = ascii_lowercase + ascii_uppercase
random.seed(1)


def get_psw(length):
    psw = ""
    for i in range(length):
        indx = random.randint(0, len(chars) - 1)
        psw += chars[indx]
    yield psw + "@mail.ru"


count = 0
while True:
    for x in get_psw(n):
        print(x)
    count += 1
    if count >= 5:
        break


