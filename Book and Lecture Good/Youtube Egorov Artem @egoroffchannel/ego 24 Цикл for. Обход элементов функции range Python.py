""" Цикл for. Обход элементов range()
Формат цикла for

for <переменная> in <объект>:
    <тело цикла>

объект должен быть итерируемым (str, list, range)

В python это более интересный цикл, который может пробегать итерируемую последовательность
Совместное использование цикла for + итерируемого объекта range()

for i in range(4):  # Обычно используют переменную i, или item
    print(i)
console:
0
1
2
3

for i in range(4):  # Обычно используют переменную i, или item
    print(i)
    i ='hello' - это изменение никак не повлияет на i, потому что цикл for будет помнить какое значение будет использоваться
print(i)  # последнее значение функции range

for i in range(100, 1000):
    if i%2 == 0 and i%7 ==0:
        print(i)
for i in range(1,11):
    print(i**2) # квадраты чисел

s = 0
for i in range(10,100): # Сумма всех двухзначных чисел можем просто менять последовательность
    s = s + i
print(s)

Факториал числа 3! = 1*2*3
pr = 1
for i in range(1,4):
    pr = pr*i
print(pr)

А как найти факториал n-го числа?
n = int(input())
pr = 1
for i in range(1,n+1):
    pr = pr * i
print(pr)

Все что до этого относиться к первому варианту,а вот далее ко второму значению

for i in range(4): # в данном случае мы просто будем выполнять инструкцию 4 раза
    print('hello')

n = int(input())
for i in range(n):
    print('hello')

Теперь создадим рандомный генератор чисел с помощью модуля random
from random import randint # импортирование

for i in range(5): # здесь 5 раз функция будет выполняться
    a = randint(1,100) #здесь интервал от 1 до 100 включительно
    print(a,end=' ')

from random import randint
s = 0
for i in range(3): # здесь 3 раз функция будет выполняться (сгенерируется a - 3 раза)
    a = randint(1,100) #здесь интервал от 1 до 100 включительно
    s +=a  # можем использовать короткую запись, мы в переменную s прибавляем сгенерированную переменную a (3 раза)
    print(a,end=' ')
print()
print(s)

Ну и вариант, когда мы с клавиатуры забираем значение:
from random import randint
s = 0   # в s сумма значений
n = int(input())
for i in range(n):
    a = randint(1,10)
    s+=a
    print(a,end=' ')
print()
print(s)

Теперь где мы используем переменную i
for i in range(1,11):
    print('x'*i)
console :
*
**
***
...
************ - 10 символов

for i in range(1,11):
    print(2**i)
console :
2
4
8
16
...
2**10 = 1024

n = int(input())
s =0
for i in range (n):
    a = int(input())
    s+=a
    print('current s:',s)
print('total',s)
print('sred arof=', s/n) #среднее арифметическое
"""