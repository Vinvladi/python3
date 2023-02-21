str_list = list(map(str,input()))
count = 0
summa = 0
for i in str_list:
    if i.isdigit() == True:
        count +=1
        summa += int(i)
print(count,summa)