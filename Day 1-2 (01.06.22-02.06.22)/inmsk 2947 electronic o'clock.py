from math import floor
import math
a = int(input())
b = int(math.floor(a/60)%24)
c = int(a%60)
print (b,c)