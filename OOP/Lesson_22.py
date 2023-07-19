class Geom:
    name = 'Geom'

    def __init__(self, x1, x2, y1, y2):
        print(f"__init__ Geom for {self.__class__}")
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print("draw line")


class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill=None):
        super().__init__(x1, x2, y1, y2)
        print("__init__Rect")
        self.fill = fill

    def draw(self):
        print("draw rect")


l = Line(0, 0, 10, 20)
r = Rect(1, 2, 3, 4)
print(l.__dict__)
print(r.__dict__)
