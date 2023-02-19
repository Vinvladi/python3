n = int(input())
count_m, count_k = 0, 0
for i in range(n):
    k_m, k_k = map(int, input().split())
    if k_m > k_k:
        count_m += 1
    elif k_m < k_k:
        count_k += 1
    else:
        count_m += 1
        count_k += 1
if count_m > count_k:
    print("Mishka")
elif count_m == count_k:
    print("Friendship is magic!^^")
else:
    print("Chris")
