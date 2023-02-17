msg = "hello python"
for idx, l in enumerate(msg):
    print(f"{idx}:{l}", end=" ")
print()
print(msg[3:])
print(msg[3:10:2])
print(msg[3::3])
print(msg[:5:2])
print(msg[::2])
print(msg[::-1])
print(msg[::-2])
print(id(msg))
msg = msg.capitalize()
print(msg)
print(id(msg))


