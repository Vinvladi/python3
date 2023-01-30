j,s = map(str,input().split)
[c for c in j]

my_string = s
start = -1
count = 0

while True:
    start = my_string.find(c, start+1)
    if start == -1:
        break
    count += 1

print (count)