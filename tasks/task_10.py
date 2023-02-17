
lst = []
for i in range(3):
    lst.append(int(input()))

print(max(lst))
print(min(lst))
lst.remove(max(lst))
lst.remove(min(lst))
print(lst[0])

