"""
Вводится таблица целых чисел.
Используя функцию map и генератор списков,
преобразуйте список строк lst_in (см. листинг)
в двумерный список с именем lst2D, содержащий целые числа.

Выводить на экран ничего не нужно, только сформировать
список lst2D на основе введенных данных.
"""

lst_in = [
    '8 11 -5',
    '3 4 10',
    '-1 -2 3',
    '-4 5 6'
]

lst_2D = [list(map(int, lst.split())) for lst in lst_in]
print(lst_2D)

