i = int(input())
c = 0
while i > 0:
    c = i%10 + c
    i = (i-(i%10)) / 10
print(c)