# '-*- coding: cp1251 -*-'
with open('my.txt') as file:  # помещаем в file все, что есть в my.txt
	print(type(file))
	for line in file:
		print(line.strip())