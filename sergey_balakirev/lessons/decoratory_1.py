import time


def func_decorator(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"work time: {dt}")
        return res

    return wrapper


@func_decorator
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@func_decorator
def get_nod_fast(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b

    return a


print(get_nod(7, 1000000521))
print(get_nod_fast(7, 1000000521))
