a = list(map(int, input().split()))
b = [3, 5, 7, 9]
if b[0] in a:
    a.remove(b[0])
if b[1] in a:
    a.remove(b[1])
if b[2] in a:
    a.remove(b[2])
if b[3] in a:
    a.remove(b[3])
print(a)
