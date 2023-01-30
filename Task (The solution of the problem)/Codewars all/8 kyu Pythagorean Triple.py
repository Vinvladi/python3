def pythagorean_triple(integers):
    integers = sorted(integers)
    a = integers[0]
    b = integers[1]
    c = integers[2]
    if a**2 + b**2 == c**2 and a>0 and b>0 and c>0:
        return True
    else:
        return False