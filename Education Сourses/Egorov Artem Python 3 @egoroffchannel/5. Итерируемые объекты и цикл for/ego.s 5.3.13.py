n = list(map(str,input()))
balance = 0
for i in n:
    if balance >= 0:
        if i == "(":
            balance +=1
        else:
            balance -=1
    else:
        break
print("YES" if balance == 0 else "NO")