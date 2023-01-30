flag = False
n = int(input())
for i in range (n):
    x = int(input())
    # if x%10 == 0
    # flag = True
    flag = (x%10 == 0) or flag
print (flag)