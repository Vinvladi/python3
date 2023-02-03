numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
summa = 0
summa = numbers[-1]
numbers.pop(-1)
summa = summa + numbers[0]
numbers.pop(0)
summa = summa + numbers[12]
numbers.pop(12)
summa = summa + numbers[7]
numbers.pop(7)
print(numbers, summa, sep="\n")