"""
Используя замыкания функций, объявите внутреннюю функцию,
которая заключает в тег h1 строку s (s - строка, параметр внутренней функции).
Далее, на вход программы поступает строка и ее нужно
поместить в тег h1 с помощью реализованного замыкания.
Результат выведите на экран.

P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>
"""


def string_teg(tag="div"):
    def do_teg(s):
        s = f"<{tag}>{s}</{tag}>"
        return s

    return do_teg


tag = input()
str_ = input()
string = string_teg(tag)
print(string(str_))