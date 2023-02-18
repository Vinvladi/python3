x = int(input())
count = 0
while x > 0:
    last = x % 10
    if last == 7:
        count += 1
    x = x // 10
print(count)
