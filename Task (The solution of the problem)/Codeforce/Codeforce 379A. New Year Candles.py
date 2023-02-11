a, b = map(int,input().split())
potuh = 0
time = 0
while a>0:
    potuh += 1
    if potuh == b:
        a += 1
        potuh = 0
    a -= 1
    time +=1
print(time)
