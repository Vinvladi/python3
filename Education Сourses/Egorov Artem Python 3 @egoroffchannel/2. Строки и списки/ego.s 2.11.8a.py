print(777 in list(map(int, input().split()))) # топ решение в одну строчку

my_list = list(map(int, input().split()))
print(my_list.count(777) > 0)