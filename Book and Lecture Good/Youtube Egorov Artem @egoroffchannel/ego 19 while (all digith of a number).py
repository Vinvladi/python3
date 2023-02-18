"""
x = int (input())
while x>0:
    print(x%10)
    x = x//10

В терминале на каждой новой строке, если число равно 4789 будет написано:
4
7
8
9

улучшим нашу задачу добавив сюда проверку (переменную, которая показывает какая у числа разрядность)
x = int(input())
kol = 0# переменная отвечающая за разрядность числа
while x>0:
    print(x%10)
    kol = kol + 1 (или просто kol += 1)
    x = x//10
print('Всего цифр:',kol)

еще улучшим нашу программу, добавим кол-во четных цифр (добавил в ego 19 + def)
x = int(input())
kol = 0
kol_ch = 0 # количество четных чисел в разрядах
while x>0:
    last =x%10
    kol += 1
    if last % 2 == 0:
        kol_ch += 1
    x = x//10
print('Всего цифр:', kol)
print('Всего четных цифр:', kol_ch)

добавим сюда еще сумму цифр числа , например для 6979, сумма числа равно 6 + 9 + 7 + 9 = 31

x = int(input())
kol = 0
kol_ch = 0
s = 0 # сумма всех чисел числа
while x>0:
    last =x%10
    kol += 1
    if last % 2 == 0:
        kol_ch += 1
    s = s + last
    x = x//10
print('Всего цифр:', kol)
print('Всего четных цифр:', kol_ch)
print('Сумма всех цифр:', kol_ch)

добавим также произведение всех цифр (переменная pr и данная переменная должна быть равна 1)

x = int(input())
kol = 0
kol_ch = 0
s = 0
pr = 1
while x>0:
    last =x%10
    kol += 1
    if last % 2 == 0:
        kol_ch += 1
    s = s + last
    pr = pr*last
    x = x//10
print('Всего цифр:', kol)
print('Всего четных цифр:', kol_ch)
print('Сумма всех цифр:', kol_ch)
print('Произведение всех цифр:', kol_ch)

Добавим 2 переменные minim и maxim самую большую цифру числа

x = int(input())
kol = 0
kol_ch = 0
s = 0
pr = 1
maxim = 0
minim = 9
while x>0:
    last = x%10
    kol = kol + 1
    if last%2 == 0
        kol_ch += 1
    s = s + last
    pr = pr*last
    if last > maxim: # все более меняем на более большое значение
        last = maxim
    if last < minim: # все больше меняем на более минимальное значение
        last = minim
    x = x//10

Дополнительно мы реализуем переход из десятичной системы в двоичную
x = int(input())
while x>0:
    last=x%2
    print(last)
    x = x//2




"""