n, m = map(int, input().split())
count = 0
kol_base = 0
if n % 2 == 0:
    for i in range(n, m + 1, 2):
        for j in range(2, int(i ** 0.5)+1):
            if i % j == 0:
                count +=1
        if count == 0:
            kol_base +=1
            print(i)
    count = 0
    if kol_base == 0:
        print("Absent")
else:
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            count += 1
    if count == 0:
        kol_base += 1
        print(n)
    for i in range(n+1, m + 1, 2):
        for j in range(2, int(i ** 0.5)+1):
            if i % j == 0:
                count +=1
        if count == 0:
            kol_base +=1
            print(i)
        count = 0
    if kol_base == 0:
        print("Absent")