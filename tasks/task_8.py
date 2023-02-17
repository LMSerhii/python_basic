class Calculator:

    def __init__(self, x, y, action):
        self.x = x
        self.y = y
        self.action = action

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def dif(self):
        return self.x / self.y

    def mul(self):
        return self.x * self.y

    def mod(self):
        return self.x % self.y

    def pow(self):
        return self.x ** self.y

    def div(self):
        return self.x // self.y

    def mathematical_action(self):
        if self.action == "+":
            print(self.add())
        elif self.action == "-":
            print(self.sub())
        elif self.action == "*":
            print(self.mul())
        elif self.action == "/":
            print(self.dif())
        elif self.action == "div":
            print(self.div())
        elif self.action == "mod":
            print(self.mod())
        elif self.action == "pow":
            print(self.pow())

try:
    x = float(input())
    y = float(input())
    action = input()
    a = Calculator(x, y, action)
    a.mathematical_action()
except Exception:
    print("Деление на 0!")