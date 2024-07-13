a = "Moscow"
b = map(lambda char: chr(ord(char) + 1), a)
c = [chr(ord(char) + 1) for char in a]
print(type(b), type(c))