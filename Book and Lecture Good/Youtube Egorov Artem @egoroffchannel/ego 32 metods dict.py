# Методы словарей
# g = {
#    1: 'one',
#    2: 'two',
#    3: 'three'
#    4: 'four'
# }
# 1) Метод g.clear(), s - словарь (данный метод очищает целиком весь словарь)
# g.clear ()
# print(g) в Shell: {}  # увидим пустой словарь
#
# 2) Метод get - получение значения
# 2.1) print(g.get(1)) в Shell: 'one'
# 2.2.a) print(g.get(5)) в Shell: None - так как 5-го значения нет.
# 2.2.b) print(g.get(5,'No such key')) в Shell: No such key  - так как 5-го ключа нет
# 2.2.b.b) print(g.get(4,'No such key')) в Shell: four      - так как есть 4-ый ключ
# 2.2.b.c) print(g.get(6,[1,2,3])) в Shell: [1,2,3]
#
# 3) Похожий на get метод setdefault - метод setdefault создает нам ключ 
# 3.1) print (g.setdefault(6))
# print(g) в Shell: {1:'one'...4:'four', 6: None} - создает 6-ой элемент 
# 3.2 Коллекции (часть 2)) g.setdefault (7,'seven') - можно использовать без print и задать определенное значение
# print(g) в Shell: {1:'one'...4:'four', 7: 'seven'}
# setdefault - по сути метод который вам создает новую пару значений, при этом если мы выводим в setdefault ключ который существует, он просто покажем нам значение ключа, без создания
#
# 4) Метод pop (Данный метод вернет нам значение 3, при этом удалив 3 ключ с значением) 
# 4.1) print (g.pop(3)) 
# print (g) 
# в Shell: three на другой строке {1:'one', 2:'two', 4:'four'}
# 4.2) print (g.pop(3)) 
# print (g.pop(2)) 
# сначало удалит 3 ключ, затем 2-ой ключ
# Код выдаст ошибку в случаях g.pop() и g.pop(5) - если элемент не существует
#
# 4.a) Метод popitem (в отличии от метода pop данный метод удаляет случайное значение из словаря, при этом возращается и сама пара и ключ и значение)
# print(g.popitem()) # в Shell : {4, 'four'} - рандомный элемент
# print(g)           # в Shell : {1: ..... 3: 'three'} - оставшиеся элементы без 4   
# В словаре элементы находится в хаотическом порядке 
# Если мы будем удалять элемент из пустого словаря, нам выведет ошибку : dictionary is empty
#
# 5) Метод keys (Метод позволяет нам получить все значения ключей)
# print(g.keys()) в Shell: dict_keys ([1,2,3,4])
# print(g.keys())
# for key in g.keys():
#   print(key, g[key])  
# в Shell на разных строках будут выведены: 1 one 2 two 3 three 4 four (без знаков и т.п.)
#
# 6) Метод values (Метод позволяющий нам получить значения value)
# print(g.values())
# for value in g.values():
#   print(value)
# в Shell на разных строках будут выведены: one two three four
#
# 7) Метод items (Данный метод возвращает все значения)
# print(g.items()) в Shell: dict_items([(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')])
# for pair in g.items():
#   print(pair) 
# в Shell на разных строках будут выведены: (1, 'one') (2, 'two') (3, 'three') (4, 'four')
#
# print(g.items())
# for pair in g.items():
#     print(pair[0],pair[1]) - вывод и ключей и эначений
#
# print(g.items())
# for key,value in g.items():
#     print(key,value) - вывод и ключей и эначений
