k = int(input())
count = 1
while count <= k:  # Задача на цикл while
    n,m = map(int,input().split())
    d = 19*m + (n + 239)*(n + 366) / 2
    count += 1
    print(int(d))