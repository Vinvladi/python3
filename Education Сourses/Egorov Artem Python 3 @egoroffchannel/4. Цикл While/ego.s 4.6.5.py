n = int(input())
d = int(input())
while n <= d:
    if n % 777 == 0:
        break
    elif n % 2 == 0:
        n += 1
        continue
    elif n % 3 == 0:
        n += 1
        continue
    else:
        print(n)
        n += 1
