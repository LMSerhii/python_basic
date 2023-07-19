import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


pt = Point(1, 2)
pt2 = Point2D(10, 20)
print(pt.__dict__)
# print(pt2.__dict__)
print(pt.__sizeof__() + pt.__dict__.__sizeof__())
print(pt.__sizeof__())

t1 = timeit.timeit(pt.calc)
t2 = timeit.timeit(pt2.calc)
print(t1, t2)