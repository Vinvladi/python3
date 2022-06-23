def massiv(n):
    a = []
    for item in range(1,n+1):
        for i in range(item,0,-1):
            a[i] = a.pop(item)


massiv(5)
