import time
import math

count = 0
k = []
for item in range(2, 1001):
    p = 1
    for d in range(2, int(math.sqrt(item) + 1), 2):
        if item % d == 0:
            p = 0
    if p == 1:
        k.append(item)
n, m = map(int, input().split())
start_time = time.time()
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
            for i in range(n, m + 1, 2):
                p = 1
                for j in range(0, len(k)):
                    if k[j] < math.sqrt(i):
                        if i % k[j] == 0:
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
            for i in range(n, m + 1, 2):
                p = 1
                for j, number in enumerate(k):
                    if i % number == 0:
                        p = 0
                if p == 1:
                    print(i)
        else:
            for i in range(n, m + 1, 2):
                p = 1
                for j, number in enumerate(k):
                    if i % number == 0:
                        p = 0
                if p == 1:
                    print(i)
print(f'Прошло {time.time() - start_time} сек')