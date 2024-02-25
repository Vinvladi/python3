"""
Кортежи абсолютно неизменяемы
"""

tuple_1 = ()  # обычный пустой кортеж

tuple_1 = ('first', "25", 25,)
# tuple[1] = 58
print(tuple)

print(tuple([45, 45, 147, 45]))
print(list((45, 45, 147, 45)))

# Словарь
dict_1 = {"Яблоко": "красное", "банан": "желтый", "лимон": "желтый"}
print(dict_1)
for key in dict_1.keys():
    print(key)
