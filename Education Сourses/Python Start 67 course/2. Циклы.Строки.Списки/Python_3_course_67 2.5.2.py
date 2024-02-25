a = list(map(int, input().split()))
b = []
if len(a) == 1:
    b = a
elif len(a) == 2:
    b.append(a[1]+a[-1])
    b.append(a[0]+a[-2])
else:
    for i in range(0, len(a), 1):
        if i == 0:
            c = a[i+1] + a[-1]
            b.append(c)
        elif i != 0 and i < len(a)-1:
            c = a[i - 1] + a[i + 1]
            b.append(c)
        elif i == len(a)-1:
            c = a[i - 1] + a[0]
            b.append(c)
for i in b:
    print(i, end=" ")

