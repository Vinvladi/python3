import math
k = []
for i in range(3, 1001, 2):
    p = 1
    for d in range(3, int(math.sqrt(i) + 1), 2):
        if i % d == 0:
            p = 0
    if p == 1:
        k.append(i)
        print(i)
print(k)
