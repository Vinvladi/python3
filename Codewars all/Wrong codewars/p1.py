def merge_arrays(arr1, arr2):
    c = []
    for item1 in arr1:
        c.append(item1)
    for item3 in range(0, len(c), 1):
        if c[item3] == c[item3 + 1]:
            c.pop(item3)
    for item2 in arr2:
        if item2 not in arr1:
            c.append(item2)

    return sorted(c)

merge_arrays([1,2,3,4], [1,2,4,5])
