# 3 -15 18 0
# 1 -7 -33 135
a,b,c,d = map (int,input().split())
if a == 0:
    for x in range (-100,101,1):
        if b*x**2+c*x+d == 0:
            print (x, end = " ")
else : 
    for x in range (-100,101,1):
        if a*x**3+b*x**2+c*x+d == 0:
            print (x,end =" ")

