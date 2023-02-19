n = int(input())
d = ""
for i in range(n):
    s = input()
    if "соль" in s:
        continue
    else:
        d = d + s +", "
print(d[0:-2])