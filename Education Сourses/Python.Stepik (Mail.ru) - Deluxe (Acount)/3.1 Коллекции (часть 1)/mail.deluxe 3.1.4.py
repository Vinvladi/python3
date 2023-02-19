n = int(input("Введите число: "))
list_n = []
for i in range(1, n+1):
    if i % 2 != 0:
        list_n.append(i)
print("Список из нечётных чисел от 1 до N:", n)