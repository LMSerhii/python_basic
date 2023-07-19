class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        print("__getitem__")
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым не отрицательным числом")
        del self.marks[key]


st1 = Student("Serhii", [1, 5, 6, 3, 4])
# print(st1.mark2s[])
# st1[10] = 17
# print(st1[2])
del st1[2]
print(st1.marks)