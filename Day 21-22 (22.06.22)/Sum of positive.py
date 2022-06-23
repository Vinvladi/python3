def positive_sum(arr):
    for item in arr:
        if item > 0:
            item += item
    return 0


positive_sum([8,7,-1])

print(positive_sum([8,7,-1]))

