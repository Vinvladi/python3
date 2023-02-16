n, m = map(int, input().split())
if n > 0 and m >0:
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    item_a, item_b = 0, 0
    result = []
    while item_a <= n - 1 and item_b <= m - 1:
        if a[item_a] <= b[item_b]:
            result.append(a[item_a])
            item_a += 1
        else:
            result.append(b[item_b])
            item_b += 1
    if a[n - 1] <= b[m - 1]:
        result.append(b[m - 1])
    else:
        result.append(a[n - 1])
    print(*result)
elif n > 0 and m == 0:
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = a
elif n == 0 and m > 0:
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = b
else:
    print(0)
