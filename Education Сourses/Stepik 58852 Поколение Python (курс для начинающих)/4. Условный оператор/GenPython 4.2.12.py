i = int(input())
if 1 <= i // 1000 <= 9 and (i%7 == 0 or i%17 == 0):
    print("YES")
else:
    print("NO")