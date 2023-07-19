string = "Hello World!!!"

print(string.upper())
""" result: HELLO WORLD!!! """
print(string.lower())
""" result: hello world!!! """
print("hello world!!".capitalize())
""" result: Hello world!!! """
print(string.replace('o', "..."))
""" result: Hell... W...rld!!! """
print(string.isalpha())
""" result: False """
print("Hello".isalpha())
""" result: True """
print("Hello".isdigit())
""" result: False """
print("5.63".isdigit())
""" result: False """
print("563".isdigit())
""" result: True """
print("hello".rjust(10, '*'))
""" result: *****hello """
print('hello'.ljust(10, '-'))
""" result: hello----- """
print(string.split())
""" result: ['Hello', 'World!!!'] """
print('-'.join(['Hello', 'World!!!']))
""" result: Hello-World!!! """
print('hello    '.strip())
""" result: 'hello' """
