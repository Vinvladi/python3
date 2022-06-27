n = int(input())
array = [] #массив данных
for num in range(n):
    x = str(input())
    array.append(x)
for item in array:
    if len(item) > 10:
        print(item[0]+str(len(item)-2)+item[-1])
    else:
        print(item)


