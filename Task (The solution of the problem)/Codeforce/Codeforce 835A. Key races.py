s, v1, v2, t1, t2 = map(int, input().split())
if (t1 + s * v1 + t1) == (t2 + s * v2 + t2):
    print("Friendship")
else:
    if (t1 + s * v1 + t1) < (t2 + s * v2 + t2):
        print("First")
    else:
        print("Second")