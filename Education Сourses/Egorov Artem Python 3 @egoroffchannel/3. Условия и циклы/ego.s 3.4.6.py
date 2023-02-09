i = int(input())
if i < 2:
    print("Младенец")
elif 2 <= i < 4:
    print("Малыш")
elif 4 <= i < 12:
    print("Ребенок")
elif 12 <= i < 19:
    print("Подросток")
elif 19 <= i < 65:
    print("Взрослый человек")
elif i >= 65:
    print("Пожилой человек")
