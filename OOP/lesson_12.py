import math

class Counter:

    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        print('__call__')
        self.__counter += 1
        return self.__counter

#
# c = Counter()
#
# c()
# c()
# c()
# c()
# res = c()
# print(res)
#


class Derivate:

    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


@Derivate
def df_sin(x):
    return math.sin(x)


# print(df_sin(math.pi/3))
# """0.8660254037844386"""
#
# df_sin = Derivate(df_sin)
# print(df_sin(math.pi/3))
# """0.49995669789693054"""

print(df_sin(math.pi/3))

