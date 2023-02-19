i = "@!#№$%&"
s = input()
n = len(s)
count = 0
for item in i: # Описание снизу здесь должно быть n-1
    for item_2 in s:
        if item in s:
            count +=1
        else:
            continue
print(count)