objs = iter([23, 78, True, 'hello'])
print(next(objs))
print(next(objs))
print(next(objs))
print(next(objs))

print(next(objs))  # мы здесь получим: исключение StopIteration, так как итератор больше 4, не может быть так как объектов только 4