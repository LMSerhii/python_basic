# N = 6
# a = [0] * N
# for i in range(N):
#     a[i] = i ** 2
#
# print(a)
#
# b = [i ** 2 for i in range(N)]
# print(b)
#
# q = input()
# s = [int(x) for x in q.split()]
# print(s)
# say = list(map(int, input(": ").split()))
# print(say)

answer = [ord(i) for i in 'python']
print(answer)

a = [x for x in range(-15, 15) if x % 2 == 0 and x % 3 == 0]
print(a)

d = [4, 3, -5, 0, 2, 11, 122, -8, 9]
a = ['четное' if x % 2 == 0 else "нечетное" for x in d]
print(a)

a = [(i, j) for i in range(3) for j in range(4)]
print(a)
a = [(i, j) for i in range(3) if i % 3 == 0 for j in range(4)]
print(a)

A = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]

A = [[x ** 2 for x in row] for row in A]

print(A)


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

A = [[row[i] for row in A] for i in range(len(A[0]))]

print(A)
