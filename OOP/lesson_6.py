from accessify import private, protected


class Point:
    # def __init__(self, x, y):
    #     self._x = x
    #     self._y = y
    def __init__(self, x, y):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y


    @private
    @classmethod
    def __check_value(cls, arg):
        return type(arg) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("not valid coordinate")

    def get_coord(self):
        return self.__x, self.__y


pt = Point('ff', 2)
print(pt.get_coord())
# pt.x = 55
# pt.y = 'dddd'
# print(pt._x, pt._y)
# print(pt.__x, pt.__y)
pt.set_coord(55,  55.66)
print(pt.get_coord())
print(dir(pt))