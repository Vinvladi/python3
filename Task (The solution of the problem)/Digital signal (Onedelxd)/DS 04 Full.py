x_n = []
y_n = []
n = 10  # сколько всего будет значений n
for i in range(0, n):  # индексы с 0-го элемента, поэтому с 0 до 9
    x_n.append(0.4 ** i - 1.6 ** (i - 1))  # x(n) = (0.4^n - 1.6^(n-1))
    if i != 0:
        y_n.append(0.5 * x_n[i] - 0.7 * y_n[i - 1])
    else:
        y_n.append(0.5 * x_n[i])
print(x_n)
print(y_n)
print(f"Готовый результат для 1 - 1")
for i in range(0, n):
    print(f'n={i}, тогда x({i}) = {round(x_n[i], 6)}, a y({i}) = {round(y_n[i], 6)}')

x_n = []
y_n = []
n = 10  # сколько всего будет значений n
for i in range(0, n):  # индексы с 0-го элемента, поэтому с 0 до 9
    x_n.append(0.4 ** i - 1.6 ** (i - 1))  # x(n) = (0.4^n - 1.6^(n-1))
    if i >= 2:  # После n>2 вся формула будет работать
        y_n.append(0.6 * x_n[i] + 0.8 * x_n[i - 1] - 1.4 * y_n[i - 1] - 1.6 * y_n[i - 2])
    elif i == 1:  # При n == 1 формула будет чуть меньше y_n[i - 2]
        y_n.append(0.6 * x_n[i] + 0.8 * x_n[i - 1] - 1.4 * y_n[i - 1])
    elif i == 0:  # При n == 0 формула будет без 0.8 * x_n[i - 1] - 1.4 * y_n[i - 1] - 1.6 * y_n[i - 2]
        y_n.append(0.6 * x_n[i])
print(x_n)
print(y_n)
print(f"Готовый результат для 1 - 2")
for i in range(0, n):
    print(f'n={i}, тогда x({i}) = {round(x_n[i], 6)}, a y({i}) = {round(y_n[i], 6)}')

x_n = []
y_n = []
n = 10  # сколько всего будет значений n
for i in range(0, n):  # индексы с 0-го элемента, поэтому с 0 до 9
    x_n.append(1.4 + 0.6 ** i)
    if i != 0:
        y_n.append(0.5 * x_n[i] - 0.7 * y_n[i - 1])
    else:
        y_n.append(0.5 * x_n[i])
print(x_n)
print(y_n)
print(f"Готовый результат для 2 - 1")
for i in range(0, n):
    print(f'n={i}, тогда x({i}) = {round(x_n[i], 6)}, a y({i}) = {round(y_n[i], 6)}')

x_n = []
y_n = []
n = 10  # сколько всего будет значений n
for i in range(0, n):  # индексы с 0-го элемента, поэтому с 0 до 9
    x_n.append(1.4 + 0.6 ** i)
    if i >= 2:  # После n>2 вся формула будет работать
        y_n.append(0.6 * x_n[i] + 0.8 * x_n[i - 1] - 1.4 * y_n[i - 1] - 1.6 * y_n[i - 2])
    elif i == 1:  # При n == 1 формула будет чуть меньше y_n[i - 2]
        y_n.append(0.6 * x_n[i] + 0.8 * x_n[i - 1] - 1.4 * y_n[i - 1])
    elif i == 0:  # При n == 0 формула будет без 0.8 * x_n[i - 1] - 1.4 * y_n[i - 1] - 1.6 * y_n[i - 2]
        y_n.append(0.6 * x_n[i])
print(x_n)
print(y_n)
print(f"Готовый результат для 2 - 2")
for i in range(0, n):
    print(f'n={i}, тогда x({i}) = {round(x_n[i], 6)}, a y({i}) = {round(y_n[i], 6)}')
