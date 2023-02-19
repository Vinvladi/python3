i1 = int(input())
i2 = int(input())
i3 = int(input())
i4 = int(input())
if i1 < i2 and i1 < i3 and i1 < i4:
    print(i1)
else:
    if i2 < i3 and i2 < i4:
        print(i2)
    else:
        if i3 < i4:
            print(i3)
        else:
            print(i4)