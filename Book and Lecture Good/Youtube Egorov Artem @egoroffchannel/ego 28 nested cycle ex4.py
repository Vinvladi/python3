# ТАБЛИЦА Умножения
""" First version
for i in range(1,10):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
"""
for i in range(1,10):
    for j in range(1,11):
        print(i,'*', j, '=', i*j, end=' ')
    print()

for j in range(1,11):  # стандартная таблица умножения
    for i in range(1,10):
        print(i,'*', j, '=', i*j, end=' ')
    print()