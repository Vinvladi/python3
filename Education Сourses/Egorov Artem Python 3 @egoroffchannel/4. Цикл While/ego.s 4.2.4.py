n = int(input())
sum_2 = int(input())
count = 1
if sum_2 < n:
    while sum_2 < n:
        sum_1 = int(input())
        sum_2 = sum_2 + sum_1
        if sum_2 > n:
            print("Довольно!")
            print(sum_2-sum_1)
            print(count)
            break
        count += 1
else:
    sum_1 = 0
    print("Довольно!")
    print(sum_2-sum_1)
    print(count)