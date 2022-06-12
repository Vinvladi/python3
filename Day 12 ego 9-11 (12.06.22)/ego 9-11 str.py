# Лекция 9-11 Все о строках
# ("hello",'hello',"hello') в IDLE Shell 'hello' и "hello" ----> результат на экране hello (исключение 'hello" - в данном случае вы не поставили закрывающийся апостров)
# (hello) Если там же написать просто hello (то будет ошибка traceback), python воспринимает это не как текст, а имя переменной, следовательно так как мы ее не создавали, будет выводится ошибка
# ('hello + enter) Если будет написано 'hello + клавиша enter, аналогично выпадет ошибка (SyntaxError)
# '''hello (результатом данных трех строчек записи будет 'hello\nworld\n456' , где \n - это перевод на новую строку (указываются после перехода на другую строку))
# world
# 456'''
# print('hello\nworld\n456') в данном случае будет написано: hello (вывод без кавычек)
#                                                            world
#                                                            456
# s1 = 'hello' (в данном случае мы сохранили строчку при помощи оператора присваивания)
# r = input()  (в данном случае пользователь сам вводит строку)
# Пример: world  r 'world' (r выведет в shell 'world')
#
# Еще пример
# d = ' ' - с использованием пробела
# e = ''
# 
# Операции со строками
# 1) Конкатенация (сцепление строк) (concatenate) (сложение строк)
# 1.1) 'abc' + 'dec'
# вывод 1.1 в Shell : 'abcdec'
# 1.2) s1+r
# вывод 1.2 в Shell : 'helloworld'
# 1.3) s1 +' '+r
# вывод 1.3 в Shell : 'hello world'
# 1.4) 'abc' + 3
# вывод 1.4 в Shell : Строки нельзя сцеплять с числом! (так как эти два разных типа не поддерживают операцию сложение)
# 1.4.1) 'abc' + str(3)  (операция str(3) сначала преобразует 3 в строку одного символа)
# вывод 1.4.1 в Shell : 'abc3'  (это правильный вариант для записи 1.4.1)
# 2) Повторение строки (или умножение (запись несколько раз))
# 2.1) 'a'* 5
# вывод 2.1 в Shell : 'aaaaa'
# 2.2) s1 * 3
# вывод 2.2 в Shell : 'hellohellohello'
# 2.3) s1 * 3.5
# вывод 2.3 в Shell : На вещественное число невозможно умножать!
# 3) Нахождение длины строки len (lenght - длина, сокращено len)
# 3.1.1) len ('abc')
# вывод 3.1.1 в Shell : 3 
# 3.1.2) len ('')  - пустая строка
# вывод 3.1.2 в Shell : 0 
# 3.1.3) len (' ')  - строка из одного пробела
# вывод 3.1.3 в Shell : 1
# 3.2) len (s1)  (Также в len можно задавать строку (s1 = 'hello'))
# вывод 3.2 в Shell : 5
# 3.3) Пример программы с input 
# s = input()  (все знаки подсчитываются, в том числе пробелы)
# print ("Вы ввели", len(s),'символов') 
# 4) Операция in (Есть ли какая подстрока в нашей строке)
# 4.1) s2 = '!@#$4567'
# Код операции in: 4 in s
# вывод 4 в Shell : True