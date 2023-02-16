test_n = int(input())  # кол-во тестов
i = 0
while i < test_n:
    n,m = map(int,input().split())
    a = input()
    b = input()
    count = 0
    if a[-1] == b[-1]:
        count += 1.5
    while len(a) >= 2:
        c = a[-2]
        d = a[-1]
        if c == d:
            count += 1
        a = a[0:-1]
    while len(b) >= 2:
        c = b[-2]
        d = b[-1]
        if c == d:
            count += 1
        b = b[0:-1]
    print("YES" if count < 2 else "NO")
    i += 1


