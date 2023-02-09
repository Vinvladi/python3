i1, i2 = input(), input()

if ((ord(i1[0]) + ord(i1[1])) % 2 == 0) and ((ord(i2[0]) + ord(i2[1])) % 2 == 0) or (
        (ord(i1[0]) + ord(i1[1])) % 2 == 1) and ((ord(i2[0]) + ord(i2[1])) % 2 == 1):
    print("YES")
else:
    print("NO")
