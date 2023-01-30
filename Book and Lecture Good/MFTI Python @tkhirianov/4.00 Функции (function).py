#    Функции
# def hello():
#   print("Hello, world")
#
# hello ()
# f = hello
# f()
#
# def hello(name):
#   print("Hello,", name)
# hello ("John")
# hello ("Alice")
# hello () - произойдет отказ
#
# Пример функции max 2 
# def max 2 (x,y):
#   if x>y:
#     return x (в современных языках программирования функция прекращает выполнение)
#   else:
#     return y
# но else можем не писать 
# def max 2 (x,y):
#   if x>y:
#     return x 
#   return y
#
# Теперь функция большая из трех, мы можем описать документацию (эта функция большая из трех)
# def max 3 (x,y,z):  (функция не только для цисел)
#   return max 2 (x, max 2 (y,z))
#
#  print (max 3(5,2,7))
#  print (max 3(1.5,0.2,17))
#  print (max 3("ab", "abc","abd")) <----- Для Duck typing
#  Duck typing (может сравнивать)
# 
# def hello_separated (name = "World", separator ="-"):
#   print ("Hello",name, sep = separator)
#
# hello_separated (separator="***", # Hello***World
#                     name = "John")
#
