# f - строка, через вложенные списки
gender = {
    'm' : 'Дорогой',
    'f' : 'Дорогая'
}

a = [
    ['Семен', 'Семенович', 32.56, 'm'],
    ['Тамара', 'Ивановна', 14.88, 'f'],
    ['Михаил', 'Анатольевич', 228, 'm'],
]

for i in a:
    print(i)
# через распакование переменных

for name,midname,balance,g in a:
    print (name,midname,balance)

for name,midname,balance,g in a:
    text = f"{gender[g]} {name} {midname}, баланс вашего лицевого счета составляет {balance} руб."
    print(text)