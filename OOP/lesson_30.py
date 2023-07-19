def func2():
    try:
        return 1 / 0
    except:
        print("func2 error")


def func1():
    try:
        return func2()
    except:
        print("func1 error")


for i in range(11):
    print("0" * 30)
    if i == 4:
        try:
            func1()
        except:
            print("func error")
