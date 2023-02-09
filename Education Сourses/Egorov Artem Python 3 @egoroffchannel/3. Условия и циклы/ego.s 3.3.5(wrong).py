import math
a = int(input())
if a % 2 == 0 and a%3 != 0:
    print(int(math.log(a,2)))
else:
    print(a)

