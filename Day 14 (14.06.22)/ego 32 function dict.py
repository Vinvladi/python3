# Какие функции поддерживают словари:
# 1) Функция del (удаление) 
# del словарь[ключ] - удаляет 1 элемент в словаре
# 2) Так как словарь является коллекцией, мы можем найти его длину по функции len, она подсчитывает сколько пар ключей значений существует в словаре
# g = {
#      1: 'one',
#      2: 'two',
#      3: 'three'
# }
# print(len(g)) в консоле Shell: 3
# 3) Функция in есть ли ключ у нас в словаре (Бинарные значения true и false)
# print (1 in g, 4 in g) в Shell: True False
# 3.a) Также можно поменять на союз not данный показатель (not in) - не содержится в ключе
# print (7 not in g)
# 
# Мы помним, если мы будем обращатся к ключу, которого у нас нет, то получим ошибку, следовательно, чтобы избежать этой ошибки
# if 5 in g: - проверяем наличие этого ключа
#   print (g[5])
# else:
#   g[5] = 'five'
# print (g)
#
# Так как словари являются коллекциями, то мы можем обходить и с помощью цикла for
# 4) for в словарях
# for key in g:
#   print(key, g[i]) - сначала ключ / потом значение ключа 