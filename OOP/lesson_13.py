class Cat:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        return f"{self.name}"


class Point:

    def __init__(self, *args):
        self.__coord = args

    def __len__(self):
        return len(self.__coord)

    def __abs__(self):
        return list(map(abs, self.__coord))


pt = Point(1, 2, -6)
print(len(pt))
print(abs(pt))