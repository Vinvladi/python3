x = int(input())
maximum = 0
while x > 0:
    last = x % 10
    if last > maximum:
        maximum = last
    if last < minimum:
        minimum = last
    x = x // 10
print(minimum, maximum, sep="\n")
