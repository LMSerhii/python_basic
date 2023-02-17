x = 0


def outer():
    x = 1

    def inner():
        nonlocal x
        x = 2
        print(x)

    inner()
    print(x)


outer()
print(x)
