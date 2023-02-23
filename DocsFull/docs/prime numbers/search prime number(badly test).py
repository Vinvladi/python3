from math import sqrt

n,m = map(int,input().split())
count = 0
good_numbers = []
for i in range(n, m+1):
    prime_numbers = True
    i_del = 2
    while i_del < sqrt(i):  # перебирать мы будем в цикле (фактически мы будем перебирать просто до sqrt)
        if i % i_del == 0:  # в таком случае число не является простым, так как простое число только делиться на себя и на 1 (5,7)
            prime_numbers = False
            break
        i_del += 1
    if prime_numbers == True and i != 4:
        good_numbers.append(i)
        count += 1
    else:
        continue
if count > 0:
    for i in good_numbers:
        print(i)
else:
    print("Absent")

