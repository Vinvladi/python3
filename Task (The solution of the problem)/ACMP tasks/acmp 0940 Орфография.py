i,n = map(str,input().split())
i = int(i)
n_1 = n.lstrip(" ")
n_new = n_1[0:i-1] + n[i:]
print(n_new)