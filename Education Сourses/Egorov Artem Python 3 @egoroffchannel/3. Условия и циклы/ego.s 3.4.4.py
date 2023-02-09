i1,i2,i3 = int(input()), int(input()), int(input())
if i1 == i2 == i3:
    print("3")
elif i1 == i2 or i2 == i3 or i1 == i3:
    print("2")
else:
    print("0")