class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        res = self.a * self.b
        return float(res)


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.p = (a + b + c) / 2

    def square(self):
        res = (self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c)) ** 0.5
        return float(res)


class Circle:
    __pi = 3.14

    def __init__(self, r):
        self.r = r

    def square(self):
        res = self.__pi * (self.r ** 2)
        return float(res)


def main():
    figure = input()
    if figure == 'треугольник':
        a = int(input())
        b = int(input())
        c = int(input())
        triangle = Triangle(a, b, c)
        print(triangle.square())
    elif figure == 'прямоугольник':
        a = int(input())
        b = int(input())
        rect = Rectangle(a, b)
        print(rect.square())
    elif figure == 'круг':
        r = int(input())
        circle = Circle(r)
        print(circle.square())


if __name__ == '__main__':
    main()