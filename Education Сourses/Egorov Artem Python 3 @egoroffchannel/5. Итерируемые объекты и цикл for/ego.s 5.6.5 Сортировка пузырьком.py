n = int(input())
d = list(map(int,input().split()))
count = 0
for j in range(n-1):
    for i in range(n-1):
        if d[i] > d[i + 1]:
            count +=1
            d[i], d[i + 1] = d[i + 1], d[i]
for i in d:
    print(i,end=' ')
print()
print(count)