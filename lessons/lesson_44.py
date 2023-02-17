""" Функции замыкания """


def say_hello(name):
    def say_goodbye():
        print(f"Goodbye my dear friend {name}")

    return say_goodbye


f = say_hello('Serhii')
f1 = say_hello(('Anton'))
f()
f1()


def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start

    return step


c1 = counter(10)
c2 = counter()

print(c1(), c2())
print(c1(), c2())
print(c1(), c2())


def strip_string(strip_chars=" "):
    def do_strip(string):
        return string.strip(strip_chars)
    return do_strip


strip1 = strip_string()
strip2 = strip_string('*-/--./ ')

print(strip1("  python!*--/ .  "))
print(strip2("  python!*--/ .  "))

