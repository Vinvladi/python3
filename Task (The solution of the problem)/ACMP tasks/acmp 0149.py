n = int(input())  # очень перегруженное решение
i_list = list(map(int, input().split()))
cd_list = i_list.copy()
cd_list.reverse()
for i in range(n):
    print(cd_list[i], sep="", end=" ") if i != n - 1 else print(cd_list[i], sep="", end="")
