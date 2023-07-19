def get_values():
    try:
        x, y = map(int, input().split())
        return x, y
    except ValueError as _ve:
        print(_ve)
        return 0, 0
    finally:
        print("finally выполняется до return")


x, y = get_values()
print(x, y)


# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError as _zde:
#     print("Деление на ноль\n", _zde)
# except ValueError as _ve:
#     print("Ошибка типа данных\n", _ve)
# else:
#     print("Исключений не произошло")
# finally:
#     print("Блок finally выполняется всегда")
#
#
# """example"""
# try:
#     file = open("example.txt")
#     file.write("hello")
# except Exception as _ex:
#     print(_ex)
# finally:
#     if file:
#         file.close()
#         print("Файл закрыт")
#
