def filter_list(l):
    d = []
    for item in l:
        if type(item) == int:
            d.append(item)
    return d


if __name__ == "__main__":
    print(filter_list([1,2,'a','b']))
