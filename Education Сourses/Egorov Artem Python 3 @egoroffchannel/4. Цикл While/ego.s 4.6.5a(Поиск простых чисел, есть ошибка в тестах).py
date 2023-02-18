n,d = map(int, input().split())
count = 0
while n <= d:
    if n % 2 == 0 and n//2 != 1:
        n += 1
        continue
    elif n % 3 == 0 and n//3 != 1:
        n += 1
        continue
    elif n % 5 == 0 and n//5 != 1:
        n += 1
        continue
    elif n % 7 == 0 and n//7 != 1:
        n += 1
        continue
    else:
        print(n)
        count += 1
        n += 1
if count == 0:
    print("Absent")