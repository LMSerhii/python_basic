lst = [x ** 2 for x in range(15)]
print(lst)

dict_ = {x: x ** 2 for x in range(15)}
print(dict_)

set_ = {x ** 2 for x in range(15)}
print(set_)

d = [1, 2, 3, 4, "1", "2", "5", -4]
a = {abs(int(x)) for x in d}
print(a)

user_name = {"jack": "15456", "lusia": "22565", "bekki": 36565, "denni": 47875}
correct_user = {key.capitalize(): int(value) for key, value in user_name.items()}
print(correct_user)
