str_gc = input()
count = 0
for i in str_gc:
    if i.upper() == "G" or i.upper() == "C":
        count += 1
print(count * 100 / len(str_gc))
