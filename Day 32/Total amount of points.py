def points(games):
    p = 0
    for c in games:
        if c[0] > c[2]:
            p = p + 3
        elif c[0] == c[2]:
            p = p + 1
        else:
            p = p
    return p


points(["1:2","3:2","4:3"])