import time

s = int(input())
j = 0
while j < s:
    g = int(input())
    good_str = input()
    count = 0
    c, c1 = [], []
    time_start = time.monotonic()
    for i in range(0, len(good_str)-1):
        item = good_str[0:i] + good_str[i+2::]
        c.append(item)
    lst1 = set(c)
    print(len(lst1))
    print(f"time{time.monotonic() - time_start}")
    j +=1