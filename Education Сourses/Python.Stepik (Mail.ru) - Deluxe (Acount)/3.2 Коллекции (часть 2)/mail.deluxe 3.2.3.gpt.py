special_symbols = "@!#№$%&"
string = input("Введите строку: ")
count = 0
for char in string:
    if char in special_symbols:
        count += 1
print(f"Количество специальных символов: {count}")