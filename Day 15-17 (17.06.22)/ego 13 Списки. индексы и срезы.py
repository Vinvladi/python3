# a =[43,54,2,54,32] - список упорядоченный набор элементов, где каждый располагается на своем конкретном месте
# Обращение к элементам списка
# 1.1)   a[0] = 43 и так далее, все также как и в строках
# 1.1.r) a[-1] = 32 (последний элемент)
# 1.2)   a[7] в Shell: list index out of range (элемент за пределами списка)
# b = [3,4,5,6,7,8,9,10,11]
# Срезы списков, аналагично строкам, примеры:  (формат <имя списка>[стартовое значение:конечное:шаг хода])
# b[1:4] = [4,5,6]   - [1..4) 
# b[1:5] = [4,5,6,7] - [1..5)
# b[2:-1] = [5,6,7,8,9,10]
# b[2:999] = [5,6,7,8,9,10,11] - возьмет все существующие значения
# b[:] = [3,4,5,6,7,8,9,10,11]
# b[::2] =[3,5,7,9,11]
# b[3:7:3] = [6,9]
# b[::-1] = [11,10,9,8,7,6,5,4,3]
# b[::-2] = [11,9,7,5,3]
# Список является изменяемым, поэтому мы можем по индексу менять его значение 
# b[2] = 100
# b после изменения Shell: [3,4,100,6,7,8,9,10,11]
# b[3:5]
# b после 2-ух изменений в Shell: [3,4,100,34,23,8,9,10,11]
# b[2:5] = 23,34 - список сотрет значение 4, так как мы его не задали
# b после 3-ех изменений в Shell: [3,4,23,34,8,9,10,11]
# del b[2]
# b в shell: [3,4,34,8,9,10,11]
# Пример с изменением списка через ссылки на 21 стр тетрадки
# a = [1,2,3] 
# d=a - просто ссылка, а вот d = a[:] создаст новый список 
