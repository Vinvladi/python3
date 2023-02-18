x = int(input())  # число в десятичной системе
to_system = 2  # мы можем в любую из систем переводить
while x > 0:
    last = x % to_system
    print(last)
    x = x // to_system
