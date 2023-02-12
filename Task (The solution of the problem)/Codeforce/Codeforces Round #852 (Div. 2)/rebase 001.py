n_1 = int(input())
k = 1
while n_1 >= k:
    a, b = map(int, input().split())
    n, m = map(int, input().split())
    price_a = a
    price_b = b
    if price_a < price_b and n <= m:
        day_1 = price_a * n
        day_2 = 0
        print(day_1 + day_2)
    else:
        z = (price_a * m) / (1 + m)
        if z <= price_b and (price_a < price_b):
            bonus = n // (m + 1)
            i = n - 1 - bonus
            j = n - i - bonus
            day_1 = i * a + j * a
            day_2 = 0
            print(day_1 + day_2)
        elif z <= price_b and (price_a > price_b):
            bonus = n // (m + 1)
            i = n - 1 - bonus
            j = n - i - bonus
            day_1 = i * a
            day_2 = j * b
            print(day_1 + day_2)
        else:
            day_1 = 0
            day_2 = price_b * n
            print(day_1 + day_2)
    k += 1