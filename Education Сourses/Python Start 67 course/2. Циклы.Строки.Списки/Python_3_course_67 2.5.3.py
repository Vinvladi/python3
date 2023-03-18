a = list(map(int, input().split()))
a.sort()
b = []
count = 0
for i in range(0, len(a)-1, 1):
    if a[i] == a[i+1]:
        count += 1
        continue
    else:
        if count != 0:
            b.append(a[i])
            count = 0
        continue
if count != 0:
    b.append(a[i])
for i in b:
    print(i, end=" ")

