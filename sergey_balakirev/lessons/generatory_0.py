a = (x ** 2 for x in range(10000000000000000000))

for i in a:
    print(i)
    if i > 50:
        break

next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)
print(next(a))


b = (x ** 3 for x in range(101))
print(list(b))
print(set(b))
c = (x ** 3 for x in range(101))
print(set(c))