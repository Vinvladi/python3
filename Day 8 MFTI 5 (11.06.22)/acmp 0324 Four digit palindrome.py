x = int(input())
b=x//1000%10
c=x//100%10
d=x//10%10
f=x%10
if b == f and c == d:
    print("YES")
else:
    print("NO")