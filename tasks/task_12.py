ticket = list(map(int, input()))

if sum(ticket[:3]) == sum(ticket[3:]):
    print("Счастливый")
else:
    print("Обычный")

