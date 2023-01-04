a, b, c = int(input()), int(input()), int(input())
d = max((a + b) * c, a + b + c, a * (b + c), a * b * c)
print(d)
