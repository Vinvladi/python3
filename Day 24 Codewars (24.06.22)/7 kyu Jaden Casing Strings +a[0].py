def to_jaden_case(string):
    ind1 = 1  # Индексы string
    ind2 = 0  # Индексы string, где Начало слова (индекс +1, так как мы можем найти повторяющиеся пробелы)
    string_good = str()  # Хорошая строка
    obl = 0 # возможно индексы хорошей строки
    c = []   # список, будем переводить все элементы строки в список
    d = []   # элементы, которые надо поднять

    if ord(string[0]) < 65 or ord(string[0]) > 90:
        for i in string:
            if i == string[0]:
                c.append(string[0].title())
                ind1 += 1
            else:
                if obl == 1:
                    obl = 0
                else:
                    c.append(i)
                if i == ' ':
                    d.append(ind1)
                    c.append(string[ind1].title())
                    i = i[:ind1] + i[ind1 + 1:]
                    obl = 1
                ind1 += 1

    else:
        for i in string:
            if obl == 1:
                obl = 0
            else:
                c.append(i)
            if i == ' ':
                d.append(ind1)
                c.append(string[ind1].title())
                i = i[:ind1] + i[ind1 + 1:]
                obl = 1
            ind1 += 1
    string_good = string_good.join(c)
    return string_good



to_jaden_case("Nids sa adswq qw")

