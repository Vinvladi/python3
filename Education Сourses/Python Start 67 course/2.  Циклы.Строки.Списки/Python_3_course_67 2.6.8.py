n = int(input())
j = 1
k = 1
for i in range(1,n+1):
    if i == k:
        print(j,end =" ")
        j +=1
        k = k + j
    else:
        print(j,end =" ")
