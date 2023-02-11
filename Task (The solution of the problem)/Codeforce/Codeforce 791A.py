ms_1,ms_2 = map(int,input().split())
n = 1
while ms_1 <= ms_2:
    ms_1 = ms_1*3*n
    ms_2 = ms_2*2*n
    n += 1
print(n-1)
