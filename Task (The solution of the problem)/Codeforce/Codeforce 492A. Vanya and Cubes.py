k = int(input())
h, count, d_count = 0, 0, 0
while d_count <= k:
    h += 1
    count = h + count
    d_count = count + d_count
print(h - 1)
