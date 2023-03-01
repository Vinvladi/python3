import time

start_time = time.time()

n, m = map(int, input().split())
count = 0
if n == m:
    p = 1
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            p = 0
    if p == 1:
        print(n)
    else:
        print("Absent")
else:
    if n % 2 == 0:
        p = 1
        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0:
                p = 0
        if p == 1:
            print(n)
            count += 1
        n += 1
        for i in range(n,m+1,2):
            p = 1
            for d in range(2, int(i ** 0.5) + 1):
                if i % d == 0:
                    p = 0
            if p == 1:
                print(i)
                count += 1
        if count == 0:
            print("Absent")
    else:
        for i in range(n,m+1,2):
            p = 1
            for d in range(2, int(i ** 0.5) + 1):
                if i % d == 0:
                    p = 0
            if p == 1:
                print(i)
                count += 1
        if count == 0:
            print("Absent")
print(f'Прошло {time.time() - start_time} сек')