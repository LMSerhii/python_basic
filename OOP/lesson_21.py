class Vector(list):

    def __str__(self):
        return " ".join(map(str, self))


v = Vector([1, 2, 3])
print(v)


class Geom:
    pass


class Line(Geom):
    pass


g = Geom()
l = Line()
print(issubclass(Line, Geom))  # Проверяет принадлежность одного класса к другому работает только с классами
print(isinstance(l, Geom))  # Проверяет  принадлежность к классам , работает и с экземплярами и классами
