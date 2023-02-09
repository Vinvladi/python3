import math
n = int(input())
a = list(map(int, input().split()))

# 1 <= k <= n-1 (1<=k <= 5
# umn = "*"
# sum = "+"
# ravn = "=="
# a[0] {ravn} a[1]
d = 0
for item in range(0,n-1,1):
    d = d + int(a[item])
    if d == math.prod(a, start=item):
        print(item)
else:
    print("-1")

# a(0) = a(1) * a(2) * a(3) * a(4) * a(5)
# else:
#   print(-1)
# n = 6
# 2 2 1 2 1 2