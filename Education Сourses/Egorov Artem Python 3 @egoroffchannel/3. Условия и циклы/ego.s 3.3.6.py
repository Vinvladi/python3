z1, z2, z3 = map(int,input().split())
if z1 >= z2 and z1 >= z3:
    if z2>= z3:
        print(z1-z3)
    else:
        print(z1-z2)
else:
    if z2>= z1 and z2>= z3:
        if z1>=z3:
            print(z2-z3)
        else:
            print(z2-z1)
    else:
        if z1>=z2:
            print(z3-z2)
        else:
            print(z3-z1)


