n = int(input())
count = 0
while n >0:
    if n == 1:
        break
    elif n%2 == 1:
        n = 3 * n + 1
        count +=1
    else:
        n = n//2
        count +=1
print(count)