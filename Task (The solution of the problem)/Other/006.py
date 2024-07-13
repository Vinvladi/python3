str_list = list(map(int,input().split()))
print(str_list)
for item in range(0, len(str_list)-1):
    if str_list[item] <= str_list[item+1]:
        d = "True"
    else:
        d = "False"
        break
print(d)