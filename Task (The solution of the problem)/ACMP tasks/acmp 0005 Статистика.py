a = int(input())
b = list(map(int, input().split()))
c = []
d = []
for item in b:
    if item % 2 != 0:
        c.append(item)
    else:
        d.append(item)
c1 = " ".join(map(str, c))
d1 = " ".join(map(str, d))
print(c1, d1, "YES" if (len(c)) <= (len(d)) else "NO", sep = "\n" )
