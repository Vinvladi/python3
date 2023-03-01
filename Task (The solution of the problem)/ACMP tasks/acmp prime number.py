import time
import math

k =[]
count = 0
n,m = map(int,input().split())
start_time = time.monotonic()
for i in range(2,int(m**0.5)+1, 1):
    p = 1
    for j in range(2, i, 1):  # проходимся обязательно до i-го элемента
        if i % j == 0:
            p = 0
    if p == 1:
        k.append(i)
if n == m:
    p = 1
    for j in k:
        if n % j == 0:
            p = 0
    if p == 1:
        print(n)
    else:
        print("Absent")
else:
    if 2 <= m-n <= 119:
        if n % 2 == 0:
            p = 1
            if n in k:
                print(n)
                count += 1
            else:
                for j in range(0, len(k)):
                    if n % k[j] == 0:
                        p = 0
                if p == 1:
                    print(n)
                    count += 1
            n = n + 1
            for i in range(n, m+1, 2):
                if i in k:
                    print(i)
                    count += 1
                else:
                    p = 1
                    for j in range(0, len(k)):
                        if i % k[j] == 0:
                            p = 0
                    if p == 1:
                        print(i)
                        count += 1
            if count == 0:
                print("Absent")
        else:
            for i in range(n, m+1, 2):
                if i in k:
                    print(i)
                    count += 1
                else:
                    p = 1
                    for j in range(0, len(k)):
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
            if n in k:
                print(n)
            else:
                for j in range(0, len(k)):
                    if n % k[j] == 0:
                        p = 0
                if p == 1:
                    print(n)
            n = n + 1
            for i in range(n, m+1, 2):
                if i in k:
                    print(i)
                else:
                    p = 1
                    for j in range(0, len(k)):
                        if i % k[j] == 0:
                            p = 0
                    if p == 1:
                        print(i)
        else:
            for i in range(n, m+1, 2):
                if i in k:
                    print(i)
                else:
                    p = 1
                    for j in range(0, len(k)):
                        if i % k[j] == 0:
                            p = 0
                    if p == 1:
                        print(i)
print(f'Прошло {time.monotonic() - start_time}')