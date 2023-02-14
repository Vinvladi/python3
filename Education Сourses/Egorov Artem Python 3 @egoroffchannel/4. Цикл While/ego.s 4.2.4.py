n = int(input())
i = int(input())
count = 1
if i < n:
    while i <= n:
        i_next = int(input())
        i = i_next + i
        if i > n:
            i = i - i_next
            print("Довольно!")
            print(i)
            print(count)
            break
        count += 1
else:
    print("Довольно!")
    print(0)
    print(0)


"""n = int(input())
sum = int(input())
count = 1
if sum < n:
    while sum < n:
        sum_1 = int(input())
        sum = sum + sum_1
        if sum > n:
            print("Довольно!")
            print(sum-sum_1)
            print(count)
            break
        count += 1
else:
    print("Довольно!")
    print(sum-sum_1)
    print(count)
"""