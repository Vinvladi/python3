input_list = list(map(str,input()))
a,b,c = 0,0,0
for i in input_list:
    if a >= 0 and b>=0 and c>=0:
        if i == "{":
            a += 1
        elif i == "}":
            a -= 1
        elif i == "[":
            b += 1
        elif i == "]":
            b -= 1
        elif i == "(":
            c += 1
        elif i == ")":
            c -= 1
    else:
        break
print("YES" if a == 0 and b == 0 and c == 0 else "NO")