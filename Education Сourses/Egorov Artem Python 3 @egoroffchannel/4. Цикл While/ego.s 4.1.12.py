x,y = map(int,input().split())
day = 1
while x < y:
    day += 1
    x = 1.15*x
print(day)