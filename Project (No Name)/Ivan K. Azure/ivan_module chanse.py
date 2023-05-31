import math
p_chance = float(input("Введите шанс: "))
q_chance = 1 - p_chance
kol = int(input("Введите количество атак: "))
p_good = []

for i in range(0,kol+1,1):
    print(f"Для kol: {i}")
    p = (math.factorial(kol))*(p_chance**i)*(q_chance**(kol-i))/(math.factorial(i)*math.factorial(kol-i))
    print(p)
    if i == 0:
        print(f"Для kol > 0:")
        print(1-p)