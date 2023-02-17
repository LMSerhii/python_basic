class Robot:
    lst1 = ['2', '3', '4']
    lst2 = ['11', '12', '13', '14', '0', '5', '6', '7', '8', '9']

    def __init__(self, n):
        self.n = n

    def verify_data(self):
        if not (0 <= int(self.n) <= 1000):
            raise TypeError("Число должно быть в диапазоне от 0 до 1000")
        return True

    def verify_language(self):

        for i in self.lst2:
            if self.n.endswith(i):
                return "программистов"
        for i in self.lst1:
            if self.n.endswith(i):
                return "программиста"
        if self.n.endswith("1"):
            return "программист"

    def get_data(self):
        self.verify_data()
        self.end = self.verify_language()
        return f"{self.n} {self.end}"


n = input()
rob = Robot(n)
print(rob.get_data())
