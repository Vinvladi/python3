# j,n = map(str,input().split()) # не работает тест xxo ukzxlzxlnqoplmvwltlkvatmnnlllxrzcuqlhgomacnpeudfjpvliodepczv # удалить одинаковые элементы
j = 'xxo'
n = 'ukzxlzxlnqoplmvwltlkvatmnnlllxrzcuqlhgomacnpeudfjpvliodepczv'
k = 0                                       
for i1 in range(0,len(j),1):
    for i2 in range (0,len(n),1):
        if (j[i1] in n[i2]) == True:
            k +=1
print (k)
