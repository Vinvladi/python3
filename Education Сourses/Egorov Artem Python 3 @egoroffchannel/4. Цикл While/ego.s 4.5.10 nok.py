a, b = map(int, input().split())
a_good = a
b_good = b
while b>0:
    c = a%b  # можно проще с помощью a,b = b,a
    a = b
    b = c
print(int(a_good*b_good/a))