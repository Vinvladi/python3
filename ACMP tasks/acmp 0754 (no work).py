m1,m2,m3 = map (int,input().split())
if 94 <= max(m1,m2,m3) <= 727 and (m1 >=94 or m2 >=94 or m3 >=94):
    print(max(m1,m2,m3))
else:
    print("Error")