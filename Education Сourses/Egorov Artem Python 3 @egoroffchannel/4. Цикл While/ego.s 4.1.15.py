i = int(input())
n = 0
while i > 1:
    if i == 1:
        n += 1
        break
    elif i % 2 == 0:
        n += 1
        i = i / 2
    else:
        n = "НЕТ"
        break
print(n)