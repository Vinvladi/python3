n_1 = int(input())
k = 1
while n_1 >= k:
    a, b = map(int, input().split())
    n, m = map(int, input().split())
    price_a = a  # перекладываем a в price_a
    price_b = b  # перекладываем a в price_a
    if price_a < price_b and n < m:
        day_1 = price_a * n
        day_2 = 0
        print(day_1 + day_2)
    else:
        z = (price_a * m) / (1 + m)
        if z <= price_b and (price_a < price_b):
            day_1 = n//(m+1) * a + (n%(m+1)) * a
            day_2 = 0
            print(day_1 + day_2)
        elif z <= price_b and (price_a > price_b):
            day_1 = n//(m+1) * m * a
            day_2 = (n%(m+1)) * b
            print(day_1 + day_2)
        else:
            day_1 = 0
            day_2 = price_b * n
            print(day_1 + day_2)
    k += 1