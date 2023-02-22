"""
Цикл for в языке Python
range - диапазон 0,1,2,3,4
for i in range(5):
    print(i)

for i in range(2,5)
    print(i)
for i in range(2,9,3): #[2,5,8]
    print(i)
for i in range(2,-1,-1): # [2,1,0]
    print(i)
for i in [2,17,35]:
    print(i)

s =[1,4,6]
for i in s:
    print(i)

for i in 'abc':
    print(i)
console:
a
b
c

s = [1,4,6]
for i in s:
    i = i + 1 #циклу все равно (таким образом изменить что-то в массиве или переменной нельзя!)

Если мы хотим менять что-то внутри массива, то тогда нам нужно работать с элементами массива
s = [1,4,6]
for i in range(len(s)): # Данный метод единственный для того, чтобы менять что-то внутри массива
    print(s[i])

Пример применения:
s = [1,4,6]
for i in range(len(s))
    s[i] = s[i] + 1

s = [1,4,6]
for i in range(2,-1,-1)
    s[i] =s[i] + 1
счетчики в основном используют i,j,k
"""