def summa_n(t):
    S = 0
    for d in range(1,t+1,1):
        S = d + S
    print(f'Я знаю, что сумма чисел от 1 до {t} равна {S}')
