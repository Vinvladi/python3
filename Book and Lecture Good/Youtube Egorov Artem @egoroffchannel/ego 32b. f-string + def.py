name = 'Семен'
mid_name = 'Семенович'
balance = 32.56

def a(i):
    return i**2

text = f"Дорогой {name} {mid_name}, баланс вашего лицевого счета составляет {balance} рублей {a(5)}"  #a () - в скобках значение, которое надо возвести в квадрат

print(text)