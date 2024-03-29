a, b = int(input()), int(input())  # Алгоритм Евклида для нахождения НОД (Наибольший общий делитель)
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)

""" 
Если у чисел НОД = 1, то такие числа называются взаимно простыми
Но проблема данного цикла в том, что если число а > b на значения больше 10000000, то цикл будет очень долго работать,
поэтому необходимо доработать данный цикл
"""