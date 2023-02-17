# import math
#
# a = int(input())
# b = int(input())
# c = int(input())
# p = (a + b + c) / 2
# S = math.sqrt(p * (p - a) * (p - b) * (p - c))
# print(S)

"""(−15,12]∪(14,17)∪[19,+∞)"""
"(a, b] - полуинтервал от а до b включая b  'a < x <= b'"
"[a, b) - полуинтервал от а до b включая a 'a <= x < b '"
"(a, b) - интервал от а до b 'a < x < b'"
"(a, +∞] - числовой луч от а до плюс бесконечности 'x >= a'"

x = int(input())
s = -15 < x <= 12 or 14 < x < 17 or x >= 19
print(s)