m,n = map(int,input().split())
i = 1
a = [] # добавляем список a - список простых числе
while m <=n:
    while i<=m: #заменим в следующей итерации программы все на i**2
        if m % i == 0:
            if i == n // i:
                a.append(i)
            else:
                a.append(i)
                a.append(n // i)
        i += 1
    m += 1
if len(a) == 0:
    print("Absent")
