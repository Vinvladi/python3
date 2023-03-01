import time
import math

start_time = time.time()

n, m = map(int, input().split())
count = 0
if n == m:
    p = 1
    for d in range(2, int(math.sqrt(n)) + 1):
        if n % d == 0:
            p = 0
    if p == 1:
        print(n)
    else:
        print("Absent")
else:
    if 2 <= m-n <= 119:
        if n % 2 == 0:
            p = 1
            for d in range(2, int(math.sqrt(n)) + 1):
                if n % d == 0:
                    p = 0
            if p == 1:
                print(n)
                count += 1
            n += 1
            for i in range(n,m+1,2):
                p = 1
                for d in range(3, int(math.sqrt(i)) + 1,2):
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
                for d in range(3, int(math.sqrt(i)) + 1,2):
                    if i % d == 0:
                        p = 0
                if p == 1:
                    print(i)
                    count += 1
            if count == 0:
                print("Absent")
    else:
        if n % 2 == 0:
            p = 1
            for d in range(2, int(math.sqrt(n)) + 1):
                if n % d == 0:
                    p = 0
            if p == 1:
                print(n)
            n += 1
            for i in range(n,m+1,2):
                p = 1
                d = 3
                while d <= int(math.sqrt(i)) + 1:
                    if i % d == 0:
                        p = 0
                    d += 2
                if p == 1:
                    print(i)
        else:
            for i in range(n,m+1,2):
                p = 1
                d = 3
                while d <= int(math.sqrt(i)) + 1:
                    if i % d == 0:
                        p = 0
                    d += 2
                if p == 1:
                    print(i)
print(f'Прошло {time.time() - start_time} сек')