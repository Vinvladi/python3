from math import sqrt

n, m = map(int, input().split())
count = 0
kol_base = 0
for i in range(n, m + 1):
    inc_i = 2
    while inc_i < sqrt(i):
        if i % inc_i == 0:
            count += 1
        inc_i += 1
    if count == 1:
        kol_base += 1
        print(i)
    count = 0
if kol_base == 0:
    print("Absent")