def get_max2(a, b):
    return a if a > b else b


a = 3
b = 5
print(get_max2(a, b))

a = 5
b = 2
c = 7
print(get_max2(a, get_max2(b, c)))


def get_max3(a, b, c):
    return get_max2(a, get_max2(b, c))


print(get_max3(a, b, c))

PERIMETR = False

if PERIMETR:
    def get_rect(a, b):
        return a + b
else:
    def get_rect(a, b):
        return a * b

print(get_rect(5, 7))
