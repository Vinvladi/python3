a = [2,1,2,3,2,1,2,3,4,2,4,3,5,3,2]
count =[0]*6
for i in a:
    count[i] += 1
print(count)
for i in range(6):  # Данный модуль выводи поочередно сколько конкретно каких элементов встречается в lust
    if count[i] > 0:
        print(i,count[i])