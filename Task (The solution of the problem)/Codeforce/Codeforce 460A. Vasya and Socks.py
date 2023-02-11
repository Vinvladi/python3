i, m = map(int,input().split())
count = i
day = 1
while count >= 1:
    count -= 1
    if day % m == 0:
        count += 1
    if count == 0:
        break
    day += 1
print(day)