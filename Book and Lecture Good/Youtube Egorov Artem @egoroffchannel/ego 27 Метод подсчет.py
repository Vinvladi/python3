"""
a = [0,1,2,3,2,1,2,3,4,2,4,3,5,3,2]
count =[0]*6
for i in a:
    count[i] += 1
print(count)

a = [2,1,2,3,2,1,2,3,4,2,4,3,5,3,2]
count =[0]*6
for i in a:
    count[i] += 1
print(count)
for i in range(6):  # Данный модуль выводи поочередно сколько конкретно каких элементов встречается в lust
    if count[i] > 0:
        print(i,count[i])

console:
[0,2,....]
0 0
1 2
2 6
...
5 1

Изменив данную программу немного мы можем отсортировать данный список:
a = [2,1,2,3,2,1,2,3,4,2,4,3,5,3,2]
count =[0]*6
for i in a:
    count[i] += 1
print(count)
for i in range(6):  # Данный модуль выводи поочередно сколько конкретно каких элементов встречается в lust
    if count[i] > 0:
        print((str(i)+' ')*count[i], end='')
# Не используется встроенная sort / sorted. Это метод подсчета при сортировке

Решим еще одну задачку, нам дана строка в которой
s = "saedasdas asda FGDH sdas wURR  %$4$*#)($)@_*"
letters=[0]*26  #0 - a, 1 - b
for i in s.lower():
    if i>="a" and i<="z" # проверкой отсекаем, все "a" <= i <= "z"
        print(i)

Но для того, чтобы было все красиво, мы должны вспомнить функцию ord
s = "saedasdas asda FGDH sdas wURR  %$4$*#)($)@_*"
letters=[0]*26  #0 - a, 1 - b
for i in s.lower():
    if i>="a" and i<="z" # проверкой отсекаем, все "a" <= i <= "z"
        print(i,ord(i))

Осталось только доделать nomer = ord(i) - 97
s = "saedasdas asda FGDH sdas wURR  %$4$*#)($)@_*"
letters=[0]*26  #0 - a, 1 - b
for i in s.lower():
    if i>="a" and i<="z" # проверкой отсекаем, все "a" <= i <= "z"
        nomer = ord(i) - 97
        letters[nomer] += 1 какие элементы присутствуют (но тут не отсортировано!)

for i in range(26):
    if letters[i] > 0
        print(i, letters[i])  #Но тут мы видим что в консоле пары
console (мой ответ может не соответствовать консольному):
0 1
1 1
2 1
...
25 1


И финальное мы должны добавить обратную функцию
Осталось только доделать nomer = ord(i) - 97
s = "saedasdas asda FGDH sdas wURR  %$4$*#)($)@_*"
letters=[0]*26  #0 - a, 1 - b
for i in s.lower():
    if i>="a" and i<="z" # проверкой отсекаем, все "a" <= i <= "z"
        nomer = ord(i) - 97
        letters[nomer] += 1 какие элементы присутствуют (но тут не отсортировано!)

for i in range(26):
    if letters[i] > 0
        print(chr(i+97), letters[i])  #Но тут мы видим что в консоле пары (добавляем chr)

Далее еще одна задача на смещение
a = []
import random
for i in range(10):
    a.append(random.randint(-10,10))

count = [0]*21
for i in a:    #здесь мы смещаемся на +10, тогда как во второй формуле мы обратно смещаемся на +10, а количество вхождений при этом остается неизменным
    count[i+10] += 1
for i in range(21):
    if count[i]>0
        print(i-10,count[i])

# Но у этого метода, есть очень большое ограничение, мы должны знать в каких пределах и сколько элементов может быть !
# так как от нашего предела зависит размер списка!
"""