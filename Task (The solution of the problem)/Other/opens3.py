
# '-*- coding: cp1251 -*-'
with open('my.txt') as file:
	for line in file:
		for symbol in line.strip(): #Пробелы и другие символы тоже
			print(symbol, ord(symbol), end=', ')
		print() #переход на следующую строку в программе, иначе все в одну строку будет выведено

x = "Hello World"
print(x)
print('Hello World')
print(type(x))
y = 9
print(type(y))