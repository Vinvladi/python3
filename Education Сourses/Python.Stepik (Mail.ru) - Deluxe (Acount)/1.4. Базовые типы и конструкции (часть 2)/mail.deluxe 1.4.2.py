i = input()
if "https" in i and "documentlibrary" in i:
    print("Адрес указан верно")
else:
    if "https" in i and "documentlibrary" not in i:
        print("подстрока documentlibrary не обнаружена.")
    elif "https" not in i and "documentlibrary" in i:
        print("адрес не начинается с https.")
    else:
        print("адрес не начинается с https. и подстрока documentlibrary не обнаружена.")