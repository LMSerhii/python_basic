"""
Ваша задача — написать функцию, которая находит сумму всех цифр в числе.
На вход также могут пойти и числа меньше нуля — их стоит переводить в неотрицательное числа.

"""


def sum_all_num(num):
    num = str(abs(num))
    count = 0
    for i in num:
        count += int(i)
    return count


# num = int(input("Enter num: "))
# print(sum_all_num(num))

num = 1234
sum_num = (num % 10) + (num // 10) % 10 + ((num // 10) // 10) % 10 + (((num // 10) // 10) // 10) % 10
print(sum_num)