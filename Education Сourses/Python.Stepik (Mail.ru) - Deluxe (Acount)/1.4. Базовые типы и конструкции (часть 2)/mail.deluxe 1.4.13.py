from random import randint # модуль для генерации случайного числа
random_number = randint(1, 10) # генерируем случайное число
user_guess = 0
count = 0
while user_guess != random_number:
    user_guess = int(input('Угадайте число от 1 до 10: '))
    if user_guess > random_number:  #  проверяем на больше, меньше
        print('Загаданное число меньше')
    elif user_guess < random_number:
        print('Загаданное число больше')
    count += 1
print(f'Вы угадали! Число попыток: {count}')