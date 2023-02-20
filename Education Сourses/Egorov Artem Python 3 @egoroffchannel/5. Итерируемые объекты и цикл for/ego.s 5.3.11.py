num = list(map(int, input()))
even = 0
odd = 0
for i in range(len(num)):
    if i % 2 == 0:
        even += num[i]
    else:
        odd += num[i]
print('YES') if (even - odd) % 11 == 0 else print('NO')