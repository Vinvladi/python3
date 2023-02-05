a, b, c = int(input()), int(input()), int(input())

if a > 0:
    if b > 0:
        if c > 0:
            print(a + b + c)
        else:
            print(a + b)
    else:
        if c > 0:
            print(a + c)
        else:
            print(a)
else:
    if b > 0:
        if c > 0:
            print(b + c)
        else:
            print(b)
    else:
        if c > 0:
            print(c)
        else:
            print("0")
