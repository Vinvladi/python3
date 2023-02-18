""" До первого улучшения
n = int(input())
i = 1
while i<n:
    if n%i == 0:
        print(i, end =' ') # отмена после каждой строки end = ' '
    i +=1
"""
""" Второе улучшение
n = int(input()) 
i = 1
while i<= n//2:
    if n%i == 0:
        print(i, end =' ') # отмена после каждой строки end = ' '
    i +=1
print(n) 
"""

"""
n = int(input())
i = 1
while i<=n**0.5: #заменим в следующей итерации программы все на i**2
    if n%i ==0
        print(i,n//i)
    i +=1
"""

"""
n = int(input())
i = 1
while i*i<=n: #заменим в следующей итерации программы все на i**2
    if n%i ==0
        if i ==n//i:
            print(i)
        else:
            print(i,n//i)
    i +=1
"""

""" Через список:
n = int(input())
i = 1
a = []
while i*i<=n: #заменим в следующей итерации программы все на i**2
    if n%i ==0:
        if i ==n//i:
            a.append(i)
        else:
            a.append(i)
            a.append(n//i)
    i +=1
a.sort()
print(a)
"""

""" Через список с еще улучшением
n = int(input())
i = 1
a = [] # добавляем список a
while i*i<=n: #заменим в следующей итерации программы все на i**2
    if n%i ==0:
        a.append(i)
        if i != n//i:
            a.append(n//i)
    i +=1
a.sort()
print(a)
"""
