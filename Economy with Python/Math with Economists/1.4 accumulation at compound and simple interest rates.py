import math
# const
fin = open('input.txt', 'r')
a = fin.readlines()
a = [line.rstrip() for line in a]
Q0 = int(a[0])  # сумма вклада
p = int(a[1])   # процент годовых
t = int(a[2])   # кол-во лет
n = int(a[3])   # сколько начислений (выплат)
N =int(input('Введите если нужно посчитать через какое время произойдет увеличение от первоначальной суммы='))
#easy
QTe = 0
QTe = Q0 * (1+(p*t)/(100*n))**n
print("Easy =",QTe,"million")
te = (N-1)/(p/100)
print("Через сколько лет сумма увеличится в n раз = ",te)
#hard
QTh = 0
QTh = Q0 * (1+p/(100*n))**(n*t)
print("Hard =",QTh,"million")
th = math.log10(N)/(n*math.log10(1+p/(100*n)))
print("Через сколько лет сумма увеличится в n раз = ",th)
#hard циклы с 1-го года по 5 по формуле сложных процентов:
for year in range(1,t+1,1):
    QThy = Q0 * (1 + p / (100 * n)) ** (n * year)
    print(year, QThy)

