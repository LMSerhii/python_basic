"""
На вход поступает строка из целых чисел,
записанных через пробел. С помощью функции map
преобразовать эту строку в список целых чисел,
взятых по модулю. Сформируйте именно
список lst из таких чисел. Отобразите его на
экране в виде набора чисел, идущих через пробел.
"""

lst = list(map(lambda x: abs(int(x)), input().split()))

# lst = list(map(abs, map(int, input().split())))
print(*lst)
