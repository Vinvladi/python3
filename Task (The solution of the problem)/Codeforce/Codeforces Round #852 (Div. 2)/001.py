n_1 = int(input())
k = 1
while n_1 >= k:
    a, b = map(int, input().split())
    n, m = map(int, input().split())
    k_1 = k_2 = 1
    while k_1 % m != 0:
        k_1 += 1
        k_2 += 1
    if a < b and k_1 > n:
        print(n * a)
    elif (k_1 + 1) * a >= k_2 * b:
        bonus = n // (k_1 + 1)
        kol = n//m
        if a >= b:
            q = (n - bonus) * a
            w = bonus * b
            price_good = w + q
            print(price_good)
        else:
            q = (n - bonus) * a
            w = bonus * b
            price_good = q + w
            print(price_good)
    else:
        print(n * b)
    k += 1
