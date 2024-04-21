def flick_switch(lst):
    n = 0
    new_list = []
    for item in lst:
        if item == 'flick':
            n += 1
            if n % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
        else:
            if n % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
    return new_list