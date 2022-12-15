def count_sheeps(sheep):
    p = 0
    for i in sheep:
        for item in i:
            if item == True:
                p =+1
            else:
                p =+0
    return p

count_sheeps([True,  True,  True,  False,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True ])