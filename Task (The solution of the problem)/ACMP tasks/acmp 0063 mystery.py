s,p = map(int,input().split())
max = 1000
min = 1
x = y = 1
for x in range(1,1001,1):    
    for y in range(x,1001,1):
        if x + y == s and x * y == p:
            if 1 <x <= y <=1000:
                print (x,y)
                break
    