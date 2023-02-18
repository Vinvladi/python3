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
""" Чуть менее понятный 
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