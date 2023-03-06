a = int(input())
b = int(input())
if b != 0:
    print(a/b)
else:
    print("Введите другое значение")
    b = int(input("Введите число не равное 0 = "))
    if b == 0:
        print("У вас не получилось ввести не нулевое значение")
    else:
        print(a/b)
