a,b,c = map(int,input().split())
if a<b:
    #a-min
    if a<c:
        print(a)
    else:
        print(c)
else:
    #b-min
    if b<c:
        print(b)
    else:
        print(c)
    