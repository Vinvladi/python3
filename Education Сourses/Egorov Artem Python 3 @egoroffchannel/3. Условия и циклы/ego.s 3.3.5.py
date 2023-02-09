a = int(input())
diagonal = 2
radius = 1
if a % 2 == 0 and a != 1:
    n = a//diagonal
    print(n)
else:
    if a != 1:
        print(a)
    else:
        print("0")

