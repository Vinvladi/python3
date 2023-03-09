def modify_list(lst):
    d = []
    for i, numbers in enumerate(lst):
        if numbers % 2 == 1:
            d.append(i)
    k = d.reverse()
    for item in d:
        lst.pop(item)
    for item,numbers in enumerate(lst):
        lst[item] = numbers//2


"""
for i in lst:
"""

lst = [1, 1, 3, 2, 4, 5, 6, 8, -1, 7, 8, 9, -16, 0, 4]
print(modify_list(lst))
print(lst)