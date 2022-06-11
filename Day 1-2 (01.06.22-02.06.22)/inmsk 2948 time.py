a = int(input())
b1 = int(a//(60*60)%24)
c1 = int(a//60%60//10)
c2 = int(a//60%60%10)
d1 = int(a%60//10)
d2 = int(a%60%10)
print ('%a:%a%a:%a%a'%(b1,c1,c2,d1,d2))
#07:47:47
