import time
start_time = time.monotonic()
k = int(input()) # test 6560
h, count, d_count = 0,0,0
while d_count <=k:
    h += 1
    count = h + count
    d_count = count + d_count
print(h-1)
print(f'Прошло {time.monotonic()-start_time}')