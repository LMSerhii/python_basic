import datetime

name = "Serhii"
birth = datetime.date(1989, 1, 29)
age = 34
print(birth)
print(f"I'm {name}, {age} years old, birth: {birth:%A, %B, %d, %Y}")
print(f"{birth} was on a {birth:%A}")

value = 1234
print(f"input={value:#06x}")
print(f"input={value:.2f}")