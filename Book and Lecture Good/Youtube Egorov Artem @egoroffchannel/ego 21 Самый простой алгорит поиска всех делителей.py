n = int(input())
i = 1
while i<n:
    if n%i == 0:
        print(i, end =' ') # отмена после каждой строки end = ' '
    i +=1

'''
проблема в том, что выполнение данного цикла будет линейным и полностью зависит от переменной n
'''