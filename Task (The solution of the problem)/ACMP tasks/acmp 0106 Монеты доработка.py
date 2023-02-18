i = int(input()) # снизил до 88 символов со 100+ в прошлой версии
s0 = s1 = c = 0
while c < i:
    d = int(input())
    if d == 0:
        s0 += 1
    else:
        s1 += 1
    c += 1
print(min(s0, s1))
