number_1 = float(input())
number_2 = float(input())
znak = input() # вводим знак
if znak =="+": # +, -, /, *, mod, pow, div
    print(number_1 + number_2)
elif znak == "-":
    print(number_1 - number_2)
elif znak == "/":
    if number_2 == 0:
        print("Деление на 0!")
    else:
        print(number_1 / number_2)
elif znak == "*":
    print(number_1 * number_2)
elif znak == "mod":
    if number_2 == 0:
        print("Деление на 0!")
    else:
        print(number_1 % number_2)
elif znak == "pow":
    print(number_1 ** number_2)
elif znak == "div":
    if number_2 == 0:
        print("Деление на 0!")
    else:
        print(number_1 // number_2)
else:
    print("Вы ввели неверный знак")