i,j = map(int,input().split())
for item in range(i-1,j,2):
    strg = str(strg) + str(item)+str(',')
print(strg)