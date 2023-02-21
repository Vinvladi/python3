a = list(map(int,input()))
count =[0]*(len(a)+1)
for i in a:
    count[i] += 1
print(count)
for i in range(6):
    if count[i] > 0:
        print(i,count[i])
