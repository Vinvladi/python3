day = int(input())
a = ["G","C","V"]
for i in range(1, day + 1, 1):
    a[2], a[1] = a[1], a[2]
    a[0], a[1] = a[1], a[0]
print(a[0],a[1],a[2], sep="")