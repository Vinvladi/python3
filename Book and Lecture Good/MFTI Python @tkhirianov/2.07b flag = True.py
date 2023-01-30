flag = True
n = int(input())
for i in range(n):
    x = int(input())
    flag = (flag and
    x%10 == 0) #можно так переносить строчку
print (flag)