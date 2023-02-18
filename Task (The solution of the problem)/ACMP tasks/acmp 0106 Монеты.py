i = int(input())
count_m = count_0 = count_1 = 0
while count_m < i:
    money = int(input())
    if money == 0:
        count_0 += 1
    else:
        count_1 += 1
    count_m += 1
if count_0 > count_1:
    print(count_1)
else:
    print(count_0)
