class Point:

    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left

    # def __getattribute__(self, item):
    #     print("__getattribute__")
    #     return object.__getattribute__(self, item)

    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError("access denied")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("attribute name not valid")
        else:
            object.__setattr__(self, key, value)

    # def __getattr__(self, item):
    #     print("__getattr__" + item)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        print("__delattr__:" + item)
        object.__delattr__(self, item)


pt = Point(1, 2)
pt1 = Point(10, 20)
# print(pt1.MAX_COORD)
# pt.set_bound(-100)
# print(pt.__dict__)
# print(Point.__dict__)
# a = pt.x
# print(a)
# pt.z = 5
# print(pt.MAX_COORD)
# print(p   t.yy)

del pt.x
print(pt.__dict__)
