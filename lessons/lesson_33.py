setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}

x = setA & setB  # setA &= setB
print(x)
y = setA | setB  # setA |= setB
print(y)
v = setA - setB  # setA -= setB
print(v)
u = setB - setA
print(u)
p = setA ^ setB
print(p)
print("=" * 50)
print(setA)
print(setB)