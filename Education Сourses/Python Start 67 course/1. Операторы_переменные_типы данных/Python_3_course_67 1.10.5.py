a = int(input())
b = int(input())
h = int(input())
if a <= h and b >= h:
    print ("Это нормально")
else:
    if a<= h and b < h:
        print("Пересып")
    else:
        print("Недосып")