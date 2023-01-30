n,k = map(int,input().split())
a,b,c = 0,0,0
a = k//n
b = k%n
c = (n - k%n)%n
print (a,b,c)