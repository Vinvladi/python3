n, m = map(int, input().split())
count = 0
kol_base = 0
for i in range(n, m + 1):
    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            count +=1
    if count == 0:
        kol_base +=1
        print(i)
    count = 0
if kol_base == 0:
    print("Absent")
