x=int(input())
a=x//100000
b=x//10000%10
c=x//1000%10
d=x//100%10
e=x//10%10
f=x%10
if (a+b+c) == (d+e+f):
    print ("YES")
else :
    print ("NO")