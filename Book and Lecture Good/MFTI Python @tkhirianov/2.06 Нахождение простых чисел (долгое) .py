n,m = map(int,input().split())
d = 0
for n in range(n,m+1,1):
    c = 0
    for m in range(1,m+1,1):
        if n%m == 0:
            c += 1
    if c == 2:
        d += 1
        print(n)
if d == 0:
    print ("Absent")