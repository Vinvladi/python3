a,b = map(int,input().split())
c,d = map(int,input().split())
if 1<=a<=8 and 1<=c<=8 and 1<=c<=8 and 1<=d<=8:
    if a == c or b == d:
        print("YES")
    else:
        print("NO")
else:
    print("NO")