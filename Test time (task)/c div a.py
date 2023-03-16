a = int(input())
b = 1
c = 1
for b in range(1,a+1):
    c = b*2/ a**b
    b +=1
    print (c,end = " ")
print (c)