x = int(input()) # где стоит координата точки
y = int(input())
if x>0:
    # 1 or 4
    if y>0:
        print(1)
    else:
        print(4)
else:
    # 2 or 3
    if y>0:
        print(2)
    else:
        print(3)