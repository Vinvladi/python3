v,t = map(int,input().split())
if 0 <= t <=1000:
    if 0 < v <= 1000:
        print (int(abs(1+v*t)%109))
    else:
        print (int(109-(abs(-1-(v*t))%109)))

