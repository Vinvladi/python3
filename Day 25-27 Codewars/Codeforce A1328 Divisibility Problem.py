import time
start_time = time.time()

n = int(input())
array = [] # создаем массив
for num in range(n): # задаем туда данные
    a, b = map(int, input().split())
    array.append(a)
    array.append(b)
for i in range(0, len(array)-1, 2):
    count = 0 # обнуляем количество шагов
    while array[i] % array[i+1] != 0: #Запомни Влад есть цикл while, не только for и if, 3 часа сидел думал!
        array[i] = array[i]+1 # бежим по циклу пока не дойдем до значения array[i] % array[i+1] != 0 и вылетаем в else
        count += 1 #считаем количество шагов
    else:
        print(count)

print("--- %s seconds ---" % (time.time() - start_time))