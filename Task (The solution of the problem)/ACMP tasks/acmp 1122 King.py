a,b = map(int,input().split())
c,d = map(int,input().split())
if 1<=a<=8 and 1<=b<=8 and 1<=c<=8 and 1<=d<=8:
# 4,5 (7,2)    
    if a-1<=c<=a+1 and b-1<=d<=b+1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")