s = input()
s_vivod = s
count = 0
for i in range(0,len(s)//2):
    if s[0] == s[-1]:
        s = s[1:-1]
        count += 1
    else:
        break
if count == len(s_vivod)//2:
    print("YES")
else:
    print("NO")