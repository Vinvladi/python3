n = int(input())
count = 0
kol_base = 0
for i in range(n+1, 2*n):
    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            count +=1
    if count == 0:
        kol_base +=1
    count = 0
print(kol_base)