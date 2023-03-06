a1 = int(input())
print(a1 > 0)  # проверяем больше ли число 0
a2 = int(input())
print(a2 >= 10 and a2 < 100)  # проверяем имеет ли число 2 разряда или нет (simplify chained comparison)
print(10 <= a2 < 100)  # более простое (цепочка из неравеств)
