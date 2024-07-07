file = open('my.txt', encoding='cp1251')
for line in file:  #Итерируемых объектов много (Мы будем бежать по строкам)
	x = line.lower().count('е')  #количество
	print(x, line.rstrip().center(30, '-'), sep='\t')