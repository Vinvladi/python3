mans = list(map(int, input().split()))
if max(mans) <= 727 and min(mans) >= 94:
    print(max(mans))
else:
    print("Error")
