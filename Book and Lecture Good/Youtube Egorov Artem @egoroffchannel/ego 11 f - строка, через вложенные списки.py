# f - строка, через вложенные списки
a = [
    ['Семен', 'Семенович', 32.56],
    ['Тамара', 'Ивановна', 14.88],
    ['Михаил', 'Анатольевич', 228],
]

for i in a:
    print(i)
# через распакование переменных

for name,midname,balance in a:
    print (name,midname,balance)

for name,midname,balance in a:
    text = f"Дорогой {name} {midname}, баланс вашего лицевого счета составляет {balance} руб."
    print(text)