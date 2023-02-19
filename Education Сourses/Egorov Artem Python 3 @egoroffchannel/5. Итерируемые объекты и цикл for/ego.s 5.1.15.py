objs = iter([23, 78, True, 'hello', [123, 433]])
print(next(objs))
print(next(objs))
print(next(objs))

print(next(objs))  # мы получим 'hello', так как это будет 4-ый вызов итератора
