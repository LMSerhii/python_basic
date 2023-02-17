s = 'python'
print(s.upper())
print(s.isupper())
print(s.lower())
print(s.islower())
print(s.count('p'))
print(s.count('h', 3, 5))
print(s.find('h'))
print(s.find('y', 4))  # если не находит элемент возвращает -1
print(s.rfind("p"))  # поиск с конца
print(s.index("p"))  # Если не находит элемент возвращает исключение
print(s.replace("p", "s"))
res = " ".join([el for el in s])
print(res)
print(res.split())
print(s.isalpha())
print("srr256".isalpha())
print("123555".isdigit())
print("12".rjust(4, '0'))
print("425f".ljust(15, "*"))
print("777".center(20, "*"))
print("    555   ".strip())
print("****555****".lstrip("*"))
print("****/555/****".rstrip("*"))


