file = open("../../data/poetry.txt")
print(file.read(4))
print(file.seek(0))
print(file.read(4))
print(file.tell())
print(file.read(4))
print(file.tell())
print(file.seek(0))
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")
for line in file:
    print(line, end="")
string = file.readlines()
print(string)
file.close()


try:
    f = open("abc.txt")
    r = f.read(1)
    f.close()
except FileNotFoundError:
    print("File Not Found")
