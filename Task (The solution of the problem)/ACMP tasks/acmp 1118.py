h, a, b = map(int, input().split())
h1 = 0
day = 0
while h1 <= h:
    h1 = h1 + a
    day += 1
    if h1 >= h:
        print(day)
        break
    else:
        h1 = h1 - b
