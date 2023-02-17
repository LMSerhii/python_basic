my_list = [*range(2, 11)]
print(my_list)
your_list = [x for x in range(10, 21)]
print(your_list)
count = 0

for x in my_list:
    count += x
print(count / len(my_list))

count = sum(your_list) / len(your_list)
print(count)

print(min(your_list))
print(max(my_list))

new_sort_list = sorted(your_list)  # старый список не меняет необходимо создать новый список
print(new_sort_list)
new_sort_list = sorted(your_list, reverse=True)
print(new_sort_list)

string_list = list('python')
print(string_list)
print(min(string_list))
print(max(string_list))
print(sorted(string_list))

print([1, 2, 3] + [2, 3])
print([1, 2, 3] + [True])
print(['I'], ['like'] * 3, ['python'])

print(7 in my_list)
print(7 in your_list)