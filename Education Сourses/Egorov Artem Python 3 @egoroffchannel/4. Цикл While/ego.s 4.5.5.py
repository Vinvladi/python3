a, b = map(int,input().split())  # Алгоритм Евклида для нахождения НОД (Наибольший общий делитель)
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print(a)