words = ['asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd']

print(" ".join(words))

fl_first = True
s = ''
for w in words:
    s += ('' if fl_first else ' ') + w
    fl_first = False
print(s)

num = [1, 6, 5, 6, 6,
       5, 8, 474, 5,
       5, 5, -15, 6,
       65, 5, 5, 45,
       454, 45, 45, 5,
       5, 4, 4, 4, 54,
       545, 45454545,
       4, 5, 54, 5, 41,
       2, 15]
for i in range(len(num)):
    if 10 <= abs(num[i]) <= 99:
        num[i] = 0

print(num)

for i, d in enumerate(num):
    if 1 <= abs(d) <= 99999999:
        num[i] = 0

print(num)