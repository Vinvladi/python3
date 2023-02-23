"""
Сколько шести-буквенных слов, начинающихся и заканчивающихся согласной буквой
и содержащих ровно 2 гласные, можно составить из букв Т, Ы, К, В, А? Каждая из допустимых букв
может входить в слово несколько раз.
"""
""" Начнем с такого:
for b1 in "tukva":
    for b2 in "tukva":
        for b3 in "tukva":
            for b4 in "tukva":
                for b5 in "tukva":
                    for b6 in "tukva":
                        print(b1,b2,b3,b4,b5,b6)
"""
count = 0
count_all = 0
for b1 in "tukva":
    for b2 in "tukva":
        for b3 in "tukva":
            for b4 in "tukva":
                for b5 in "tukva":
                    for b6 in "tukva":
                        count_all +=1
                        rez = b1 + b2 + b3 + b4 + b5 + b6
                        if rez[0] in 'tkv' and rez[-1] in 'tkv':
                            if rez.count('a') + rez.count('u') == 2:
                                count +=1
print(count)
print(f'{count} из {count_all} это {count/count_all} %')