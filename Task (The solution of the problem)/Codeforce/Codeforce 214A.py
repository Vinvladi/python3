n,m = map(int, input().split())
k = max(n,m)
count = 0
for a in range(0,k+1,1):
    for b in range(0,k+1,1):
        if a**2 + b == n and a + b**2 == m:
            count += 1
print(count)
