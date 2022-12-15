principal = 1000 # Исходная сумма
rate = 0.05      # Процентная ставка
numyears = 5     # Количество лет
years = 1
while years <= numyears:
    principal = principal*(1+rate)
    print(years,principal)
    years +=1
