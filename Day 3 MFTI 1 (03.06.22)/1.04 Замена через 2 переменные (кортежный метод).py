# Замена через 2 переменные кортежным методом
a = 2
b = 5
tmp1, tmp2 = b,a
a,b = tmp1,tmp2
print (a,b)
# или
a,b = b,a # Это обмен с двумя дополнительными переменными (обмен через временный кортеж), как вычислится a,b 