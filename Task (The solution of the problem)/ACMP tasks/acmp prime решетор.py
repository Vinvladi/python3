import math


n = 1000000
n,m = map(int,input().split())
a = [i for i in range(n+1)]
a[1] = 0
i = 2
while i <= int(math.sqrt(n)+1):
    if a[i] != 0:
        j = i + i
        while j <= n:
            a[j] = 0
            j += i
    i += 1
a = [i for i in a if i != 0]



count = 0
for i in range(n,m+1,1):
    if i in a:
        print(i)
        count += 1
if count == 0:
    print("Absent")
