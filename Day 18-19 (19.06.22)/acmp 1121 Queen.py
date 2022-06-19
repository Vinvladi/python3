from base64 import b16encode


a,b = map(int,input().split())
c,d = map(int,input().split())
if 1<=a<=8 and 1<=b<=8 and 1<=c<=8 and 1<=d<=8:
# 4,5 (7,2)    
    if a+b==c+d or a-b == c-d or a == c or b == d:
        print("YES")
    else:
        print("NO")
else:
    print("NO")