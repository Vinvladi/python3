# Глобальный документ по изучению python.

1) Тема типы данных 

| Синтаксис    | Тип данных               | Пример               |
|---------|--------------------|-------------------------|
| int     | Целые числа        | -20, 0, 50, 100_000_100 |
| float   | Вещественные числа | --------                |
| complex | Комплексные числа  | True / False            |
| str     | Строка             | dsewrew12,fgdew1        |
| bool    | Логический тип     | True / False            |
```
Вещественные могут быть как рациональными, так и иррациональными числами
```
Основные математические операции:

| Синтаксис | Тип данных             | Пример                                                   |
|-----------|------------------------|----------------------------------------------------------|
| a + b     | Операция сложения      | int, если оба числа int<br/>float, если одно число float |
| -a        | Унарный минус          | int, если оба числа int<br/>float, если одно число float |
| a - b     | Операция разность      | --------                                                 |
| a * b     | Операция умножение     | int или float                                            |
| a / b     | Операция деление       | float                                                    |
| a // b    | Операция деления (div) | True / False                                             |
| a % b     | Операция деления (mod) | True / False                                             |
| a ** b    | Умножение в степень    | True / False                                             |

Методы строк. Первый объект после математических чисел, которые я изучил.


Содержание:

# Модуль строк
```
Таблица № 1 Строки base methods.
```
| Название                               | Пример кода:                             | Терминал:   | Выполнение программы (local)           |                                                                       Link Github |
|:---------------------------------------|------------------------------------------|-------------|----------------------------------------|----------------------------------------------------------------------------------:|
| Конкатенация ver 1(s+r)                | s="hello"<br/>r="world"<br/>print(s+" "+r) | hello world | ```python docs\string\string.1.0.py``` | [Code](https://github.com/Vinvladi/python3/blob/main/DocsFull/docs/string/string.1.0.py) |
| Конкатенация ver 2(k+d)                | k = "abc"<br/>d=str(3)                   | abc3        | ```python docs\string\string.1.1.py```        | [Code](https://github.com/Vinvladi/python3/blob/main/DocsFull/docs/string/string.1.1.py) |
| Операция нахождения длины строки (len) | s = 'abc'<br/>print(len(s))              | 3           | ```python docs\string\string.1.2.py```        | [Code](https://github.com/Vinvladi/python3/blob/main/DocsFull/docs/string/string.1.2.py) |
| Операция (ord)                         | s = 'a'<br/>print(ord(s))                | 97          | ```python docs\string\string.1.3.py```        | [Code](https://github.com/Vinvladi/python3/blob/main/DocsFull/docs/string/string.1.3.py) |
```
Конкатенация (concatenate - сцеплять, сцепление строк)
Операция ord возвращает к коду элемента соответсвующему таблице: ascii code table
```
