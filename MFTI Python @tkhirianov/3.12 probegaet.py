# Напишем программу, которая собирает цифры из числа (с конца последовательно)
base = 10
x = int(input())
while x>0:
    digit = x%base #добыли последнюю цифру
    print(digit, end=" ") #подряд с пробелом
    x //= base #x+=5 <=> x=x+5 (это отрывает 1 цифру)