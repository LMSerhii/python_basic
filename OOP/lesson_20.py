class Geom:
    name = 'Geom'

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print("Рисование примитива")


class Line(Geom):
    name = 'Line'

    def draw(self):
        print("Рисование линии")


class Rect(Geom):
    def draw(self):
        print("Рисование прямоугольника")


l = Line()
r = Rect()
print(l.name)
print(r.name)
l.set_coords(1, 1, 2, 2)
r.set_coords(1, 1, 2, 2)
print(l.__dict__)
print(r.__dict__)
l.draw()
r.draw()