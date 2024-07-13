def triple_performer(function, x):
	print(function(x)) #вызов функции 3 раза по отношению к x
	print(function(x))
	print(function(x))

triple_performer(lambda x: x[:5], "Ничего на свете лучше нету, чем купить у друга сигарету") # функция над объектом срезать первые 5-элементов
triple_performer(lambda x: x.upper(), "Ничего на свете лучше нету, чем купить у друга сигарету")