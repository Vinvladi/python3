"""
Напишите программу, которая генерирует случайное целое число в диапазоне от 1 до 10 и запрашивает
у пользователя число до тех пор, пока он его не отгадает. Выводите сообщения в соответствии с примером.
используй библиотеку from random import randint
Ответ GPT chat:
from random import randint
random_number = randint(1, 10)
user_guess = 0
while user_guess != random_number:
    user_guess = int(input('Угадайте число от 1 до 10: '))
    if user_guess > random_number:
        print('Загаданное число меньше')
    elif user_guess < random_number:
        print('Загаданное число больше')
print('Вы угадали!')
"""

# Доработанная версия с f стройкой в выводе
from random import randint
random_number = randint(1, 10)
user_guess = 0
count = 0
while user_guess != random_number:
    user_guess = int(input('Угадайте число от 1 до 10: '))
    if user_guess > random_number:
        print('Загаданное число меньше')
    elif user_guess < random_number:
        print('Загаданное число больше')
    count += 1
print(f'Вы угадали! Число попыток: {count}')