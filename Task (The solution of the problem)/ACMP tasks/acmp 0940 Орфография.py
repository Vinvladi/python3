i,n = map(str,input().split()) # при этом i у нас является int
i = int(i)
n_1 = n.lstrip(" ")
n_new = n_1[0:i-1] + n[i:]
print(n_new)