# '-*- coding: cp1251 -*-'
with open('my.txt') as file:  # �������� � file ���, ��� ���� � my.txt
	print(type(file))
	for line in file:
		print(line.strip())