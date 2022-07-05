import math
n,m,a = map(int,input().split())
c1,c2 = 0,0
if n > a:
    c1 = math.ceil(n/a)
else:
    c1 = 1
if m > a:
    c2 = math.ceil(m/a)
else:
    c2 = 1
print(c1*c2)