lst = ['0', '1', '2', '3', '4', '5', '6']
lst2 = ['zero', 'first', 'second', 'third', 'forth', 'fifth', 'sixth']
a = dict.fromkeys(lst)
print(a)
a = dict.fromkeys(lst, lst2)
print(a)

d = a.get("7")
print(d)
d = a.get("7", "no data")
print(d)

print(a.setdefault("7", "seventh"))
print(a)

print(a.pop("4", "ключа больше нет "))

lis = [*range(1, 1000000)]
print(f"{type(lis)}{lis.__sizeof__()}")
tp = tuple(lis)
print(f"{type(tp)}{tp.__sizeof__()}")

lis = [1, 2, 3]
print(f"{type(lis)}{lis.__sizeof__()}")
tp = (1, 2, 3)
print(f"{type(tp)}{tp.__sizeof__()}")
