
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

A = 1, 2, 3
x, y, z = A
print(x, y, z)
print(A, type(A))

a,b,c,d, *rest = "Goodby, my dear friend!"
print(a,b,c,d)
print(rest)
print(type(rest))

*rest, a, b, c = [1,2,3,4,5,6,7,8,9,10]
print(a, b, c)
print(rest)