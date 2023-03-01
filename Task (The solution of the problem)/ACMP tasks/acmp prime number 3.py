import time
import math


count = 0
n,m = map(int,input().split())
start_time = time.monotonic()
A = [True]*1000000
A[0] = A[1] = False
for k in range(2,1000000):
    if A[k]:
        for m in range(2*k,1000000,k):
            A[m] = False
for k in range(m):
    print(k,'-','простое' if A[k] else 'составное')
print(f'Прошло {time.monotonic() - start_time}')