"""
i = 1
while True:
    print('Итерация №',i)
    if i==10:
        break  # программа закончиться полностью выйдя из цикла
        print('hi')
    i +=1
print('hello')
"""
"""
while True:
    a = input()
    if a =='exit':
        break
    print(a, len(a))
"""
""" Теперь с модулем continue
while True:
    a = input()
    if a=='exit':
        break
    if len(a)<5:
        continue  #  в отличии от break continue перекидывает нас в начало цикла 
    print(a, len(a))
"""
""" While + else
i = 1
while i<=15:
    print(i)
    i += 1
else:
    print('good')
    print('job')
print('end')
"""

""" While + else
i = 1
while i<=15:
    print(i)
    i += 1
else:
    print('good')
    print('job')
print('end')
# Важно: Что блок else в питоне будет выполняться, только в том случае, когда цикл завершится сам по себе, то есть без
принудительного выхода. 
"""

""" While + else + break
i = 1
while i<=15:
    print(i)
    if i ==5:
        break (то после break все что находиться ниже до выхода из цикла будет пропущено все в else (print('good') и print('job'))
    i += 1
else:
    print('good')
    print('job')
print('end')
# Важно: Что блок else в питоне будет выполняться, только в том случае, когда цикл завершится сам по себе, то есть без
принудительного выхода. 
"""

""" Пример применение while + else + break
a = [54,32,65,765,32,543]  # Нам необходимо написать программу если все четные числа вывести "YES" и "No" в противном случае 
##Yes - все четные
##No - в противном случае
while len(a)>0:
    last = a.pop() - мы берем последний элемент (метод в ego 14) / все с конца мы берем
    if last%2 != 0:
        print('No', last) # нам нужно вывести no, если у нас хотя бы один элемент нечетный , last - первый попавшийся с конца элемент
        break
else:
    print("YES")
"""