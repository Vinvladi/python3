# Списки и операции над ними 
# Списки представляют собой упорядоченый набор элементов, позволяющий хранить взаимосвязанные данные
# marks=[4,5,3,4,5]
# t1 = 20
# t2 = 24
#t_july = [20,24,30,25,15,23]
# Списки хороши тем, что мы можем хранить в нем разные типы переменных
# a =[True,43,'hello',[4,5,6]]
# b =[] - пустой список
# type(b) в Shell: <class 'list'>
#
# ОПЕРАЦИИ НАД СПИСКАМИ
# 1) len - длина списка (количество элементов)
# 1.1) Операция длины списка len([1,2,3]) в Shell: 3
# 1.2) len(b) в Shell: 0
# 1.3) len(a) в Shell: 4
# 2) Сцепление списков
# [12,23] + [1,2,3] в Shell: [12,23,1,2,3]
# за счет данной операции, мы можем расширять список
# 2.1) a = a + [4]     в Shell : [True,43,'hello',[4,5,6],4] - сцепление в конец списка
# 2.2) a = ['hi'] + a  в Shell : ['hi',True,43,'hello',[4,5,6],4]
# 2.3.w) [1,2,3,4] + 4 в Shell : TypeError
# 3) Дублирование списка
# 3.1) [a]*4, умножать списки на вещественные числа нельзя
# в Shell 3.1: [True,43,'hello',[4,5,6],4,True,43,'hello',[4,5,6],4,True,43,'hello',[4,5,6],4,True,43,'hello',[4,5,6],4]
# 4) Проверка вхождения
# 4.1) 43 in a      | в Shell: True
# 4.2) 'ht' in a    | в Shell: False 
# 4.3) [4,5,6] in a | в Shell: True
# 4.4) [4,5] in a   | в Shell: False (если мы будем искать часть [4,5,6], то мы не найдем)
# 
# 5) Если список числовой, то мы можем использовать дополнительные операции
# w =[43,54,65,3,4,65,-43,32]
# 5.1) max(w)
# Операции максимального элемента списка: max(w) в Shell: 65
# 5.2) min(w) - нахождение минимального элемента в списке
# min(w) в Shell: -43
# 5.3) sum(w) (int,float)
# 5.3.1) sum (w) в Shell: 223
# 5.3.2) sum([1,2,3,4]) в Shell : 10
# 5.4) sorted - сортировка списка (отсортировать список) 
# 5.4. возврастанию) sorted(w), по умолчанию список сортирует по умолчанию элементов :
# 5.4.убыванию) sorted(w,reverse=True) 
# ОЧЕНЬ важно, что при сумме, максимуме, сортировке и минимуме были нужные типы данных
#
# 6) Сравнение списком между собой:
# 6.1) [100,54] > [34,543,654,43] в Shell: True (Все потому что, элементы списка сравниваются также как и элементы строки, то есть берутся первые элементы из списков) =>
# что мы фактически сравниваем [100] > [34] , остальные элементы вообще не участвуют в сравнении
# в случае 6.1.b) [1,2,3] > [1,2,'re'] в Shell: TypeError ('int' and 'str') нельзя сравнивать 2 разных типа переменных
# 6.2) аналогично списки будут совпадать, если будут совпадать все элементы списка и их количество элементов
#
# 7) Среднее значение : sum(...)/len(...)
# 7.1) sum(marks)/len(marks) в Shell: 4.2 (Это значение float)