h,a,b = map(int,input().split())
k = 0
day1 = a
day = 0
if 0 < h <= 1000 and 0 < a <=100 and 0 < b <=100:
    if day1+day <= h:
        day += a-b
        print(day)