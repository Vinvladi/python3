
lst = [1, 2, 3]

def add_to_list(lst, new_value):

    lst = lst.append(new_value)

    return lst

add_to_list(lst, 4)

print(lst)