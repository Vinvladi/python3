n = int(input())
s = 1
if n == 0:
    print("1")
else:
    for item in range(1, n+1, 1):
        s = s * item
    print(s)