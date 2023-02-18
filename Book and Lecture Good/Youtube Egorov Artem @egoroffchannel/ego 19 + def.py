def number_of_digits(x):  # функция считает сколько у нас всего разрядов у числа
    num_digits = 0
    while x > 0:
        num_digits += 1
        x = x // 10
    return num_digits


def number_of_even_number(x):  # количество четных чисел в разрядах числа
    count_even_number = 0
    while x > 0:
        last = x % 10
        if last % 2 == 10:
            count_even_number += 1
        x = x // 10
    return count_even_number


def number_decomposition(x):  # разложение на разряды
    number_decomposition_list = []
    while x > 0:
        decomposition_number = x % 10
        number_decomposition_list.append(decomposition_number)
        x = x // 10
    return number_decomposition_list  # мы получим обратный список, если число: 6946, то на выходе в терминале мы получим 6,9,4,6


def number_good_decomposition(x):  # получаем в правильном расположении лист с элементами list с элементами
    number_good_decomposition_list = []
    while x > 0:
        decomposition_number = x % 10
        number_good_decomposition_list.append(decomposition_number)
        x = x // 10
    number_good_decomposition_list.reverse()
    return number_good_decomposition_list


def sum_number_of_digit_ver_1(x):
    sum_number_v1 = 0
    while x > 0:
        last_element_sum = x % 10  # непосредственно последний элемент для суммы сумма начинается с конца
        sum_number_v1 = sum_number_v1 + last_element_sum
        x = x // 10
    return sum_number_v1


def sum_number_of_digit_ver_2(x):
    sum_list = []
    while x > 0:
        last_element_sum = x % 10  # непосредственно последний элемент для суммы сумма начинается с конца
        sum_list.append(last_element_sum)
        x = x // 10
    sum_number_v2 = sum(sum_list)
    return sum_number_v2


def multiplication_of_digit_ver_1(x):
    multiplication_digit = 1
    while x > 0:
        last_element_multiplication = x % 10  # последний элемент для умножения
        multiplication_digit = last_element_multiplication * multiplication_digit
        x = x // 10
    return multiplication_digit


def digit_maximum(x):
    maximum = 0
    while x > 0:
        last = x % 10
        if last > maximum:
            maximum = last
        x = x // 10
    return maximum


def digit_minimum(x):
    minimum = 9
    while x > 0:
        last = x % 10
        if last < minimum:
            minimum = last
        x = x // 10
    return minimum


def digit_10_to_2(x):
    digit_to_2 = []
    while x > 0:
        last = x % 10
        digit_to_2.append(last)
        x = x // 10
    digit_to_2.reverse()
    return digit_to_2


x = int(input())  # все берем из одного числа
number_of_digits(x)  # вызов функции number_of_digits от числа i
number_of_even_number(x)  # вызов функции четных чисел в разрядах числа x
number_decomposition(x)  # вызов функции, которая в конечном итоге выдает list со всеми цифрами числа
number_good_decomposition(x)  # вызов функции, которая в конечном итоге выдает
# list со всеми цифрами числа в правильном порядке
sum_number_of_digit_ver_1(x)  # первая версия egorov 19 лекция youtube сумма всех цифр числа
sum_number_of_digit_ver_2(x)  # вторая версия, написанная непосредственно мной
multiplication_of_digit_ver_1(x)  # умножение числа
digit_maximum(x)  # максимальная цифра числа
digit_minimum(x)  # минимальная цифра числа
digit_10_to_2(x)  # перевод числа в двоичную систему

print(
    f'Сколько разрядов у числа {x}? Разрядов = {number_of_digits(x)} \n'
    f'Сколько четных чисел в разрядах числа {x}? Количество четных разрядов {number_of_even_number(x)} \n'
    f'Разложение на список всех цифр числа обратная запись: {number_decomposition(x)}, а вот прямая:{number_good_decomposition(x)} \n'
    f'Сумма всех цифр числа = {sum_number_of_digit_ver_1(x)} - Egorov, {sum_number_of_digit_ver_2(x)} -  моя версия \n'
    f'Умножение всех цифр числа = {multiplication_of_digit_ver_1(x)})'
    f'Самая большая цифра числа = {digit_maximum(x)}, а тут самая маленькая = {digit_minimum(x)} '
    f'Десятичная форма записи числа переводится в двоичную (list) = {digit_10_to_2(x)}')
