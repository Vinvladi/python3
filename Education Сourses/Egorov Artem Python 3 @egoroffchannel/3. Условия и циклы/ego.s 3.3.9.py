a,b = input(),input()
a = a.lower()
b = b.lower()
if a[-1] == "ь":
    if a[-2] == b[0]:
        print("Good")
    else:
        print("Bad")
else:
    if a[-1] == b[0]:
        print("Good")
    else:
        print("Bad")
