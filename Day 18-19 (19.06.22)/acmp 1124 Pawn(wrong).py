a,b = map(int,input().split())
c,d = map(int,input().split())
if 1<=a<=8 and 1<=b<=8 and 1<=c<=8 and 1<=d<=8:
    if b == 2:
        if a == c and (b+2 == d or b+1 ==d):
            print("YES")
        else:
            print("NO")
    else:
        if a == c and (b+1 == d) :
            print("YES")
        else:
            print("NO")
else:
    print("NO")