a = int(input())
c = []
n = 0
d = []
sum_diog = 0
while n < a:
    b = list(map(int, input().split()))
    c.append(b)
    n += 1
for i in range(a):
    for j in range(a):
        print(c[-j-1][-i-1], end=' ')
    print()
