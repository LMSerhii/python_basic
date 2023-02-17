# true_psw = 'password'
# ps=''
#
# while ps != true_psw:
#     ps = input("Введите пароль: ")
#
# print("Вход в систему")
#
d = [1, 6, 95, 5, 4, 0, -1, -2]
i = 0
flagFind = False

while i <= len(d):
    flagFind = d[i] % 7 == 0
    if flagFind:
        break
    i += 1

print(flagFind)
