lst = ['Kyiv', 'Kharkiv', 'London', 'Los Angeles']
a = lst[2:3]
print(a)
print(lst)
lst[3] = 'Lviv'
print(lst)

copy_lst = lst[:]
print(id(lst), lst)
print(id(copy_lst), copy_lst)

d = lst
print(id(lst), lst)
print(id(d), d)

number_list = [1, 2, 3, 4, 5, 6]
print(number_list[2:-1])
print(number_list[-3:-1])
print(number_list[1:5:2])
print(number_list[:5:2])
print(number_list[1::2])
print(number_list[::2])
print(number_list[::-1])

number_list[2:4] = ['good', 'very good']
print(number_list)
number_list[:2] = 100, 200
print(number_list)

print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] != [1, 2, 3])
print([1, 2, 3] > [1, 2, 3])
print([15, 2, 3] > [1, 2, 3])
