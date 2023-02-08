a, b = int(input()), int(input())
maximum = a if a >= b else b
minimum = a if a < b else b
print(f'{minimum} {maximum}')
