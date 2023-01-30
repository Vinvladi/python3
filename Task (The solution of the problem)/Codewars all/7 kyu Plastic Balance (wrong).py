import math

def plastic_balance(list):
    for k in range(0, math.floor(len([list])/2), 1):
        if list[0] + list[-1] != sum(list[1:-1]):
            list = list.pop(0).pop(-1)
            if len(list) == 0:
                return []
        print(k)
        if list[0] + list[-1] == sum(list[1:-1]):
            return print("Yes")


plastic_balance([0, 104, 3, 101, 0, 111])
