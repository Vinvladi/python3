#Сначало функция
def is_simple_number (x):
    divisor = 2
    while divisor < x:
        if x%divisor == 0:
            return False
        divisor +=1
    return True

x = int(input())            #вводим значение переменной
print (is_simple_number(x)) #выводим, то что будет после переменной

# Метод грубой силы (bruteforce)
# является ли число простым, если число простое, то возвращает Thue, a иначе - False.
# x - целое положительное число.