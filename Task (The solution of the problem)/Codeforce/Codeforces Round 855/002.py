"""
s = "saedasdas asda FGDH sdas wURR  %$4$*#)($)@_*"
letters=[0]*52  #0 - a, 1 - b
for i in s:
    if (i>="a" and i<="z") or (i>="A" and i<="Z"): # проверкой отсекаем, все "a" <= i <= "z"
        nomer = ord(i) - 122
        letters[nomer] += 1  #какие элементы присутствуют (но тут не отсортировано!)

for i in range(52):
    if letters[i] > 0:
        print(i, letters[i])  #Но тут мы видим что в консоле пары
"""