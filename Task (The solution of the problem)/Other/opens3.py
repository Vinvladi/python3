
# '-*- coding: cp1251 -*-'
with open('my.txt') as file:
	for line in file:
		for symbol in line.strip(): #������� � ������ ������� ����
			print(symbol, ord(symbol), end=', ')
		print() #������� �� ��������� ������ � ���������, ����� ��� � ���� ������ ����� ��������

x = "Hello World"
print(x)
print('Hello World')
print(type(x))
y = 9
print(type(y))