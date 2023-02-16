n, k = map(int, input().split())
w = 0  # w - время решенных задач
count = 0  # - количество решенных задач
while w + k < 60 * 4:
    count += 1
    w = count * 5 + w
    if count == n + 1:
        break
if w + k > 240 or count > n:
    print(count - 1)
else:
    print(count)
