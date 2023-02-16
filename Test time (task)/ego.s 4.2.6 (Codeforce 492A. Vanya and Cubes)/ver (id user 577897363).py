import time
start_time = time.monotonic()
n = int(input()) # test 6560
total = 0
step = 1
what = 0
while what + step <= n:
    step += 1
    total += step
    what += total
print(step - 1)
print(f'Прошло {time.monotonic()-start_time}')