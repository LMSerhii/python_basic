class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Seconds must be integer')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.get_formatted(h)}:{self.get_formatted(m)}:{self.get_formatted(s)}"

    @classmethod
    def get_formatted(cls, x):
        return str(x).rjust(2, '0')

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("right operand must be int or Clock")
        return other if isinstance(other, int) else other.seconds

    def __add__(self, other):
        sc = self.__verify_data(other)
        return Clock(self.seconds + sc)

    def __mul__(self, other):
        sc = self.__verify_data(other)
        return Clock(self.seconds * sc)

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    def __iadd__(self, other):
        sc = self.__verify_data(other)
        self.seconds += sc
        return self

    def __imul__(self, other):
        sc = self.__verify_data(other)
        self.seconds *= sc
        return self


time = Clock(1000)
# time2 = Clock(2000)
# time = time + time2
# time = time + 100
# time = 100 + time
# time += 100

# time = time * 10
# time = 10 * time
time *= 10
print(time.get_time())

