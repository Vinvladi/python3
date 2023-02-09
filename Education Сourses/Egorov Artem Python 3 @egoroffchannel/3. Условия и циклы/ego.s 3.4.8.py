p1, p2 = input(), input()
if len(p1) < 7:
    print("Short")
elif p1 == p2:
    print("OK")
else:
    print("Difference")
