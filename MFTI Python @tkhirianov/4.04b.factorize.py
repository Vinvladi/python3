def factorice_number (x): #расскадывает число на множители // печатает их на экран //x- целое число
    divisor = 2
    while x>1:
        if x%divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor +=1

x=int(input())
factorice_number (x)