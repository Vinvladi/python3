s = int(input())
i = 0
while i<s:
    d = input()
    m = e = o = w = 0
    string_good = input()
    string_good = string_good.lower()
    while len(string_good) > 0:
        if string_good[0] == "m":
            string_good = string_good[1::]
            m = 1
            continue
        else:
            break
    while len(string_good) > 0:
        if string_good[0] == "e":
            string_good = string_good[1::]
            e = 1
            continue
        else:
            break
    while len(string_good) > 0:
        if string_good[0] == "o":
            string_good = string_good[1::]
            o = 1
            continue
        else:
            break
    while len(string_good) > 0:
        if string_good[0] == "w":
            string_good = string_good[1::]
            w = 1
            continue
        else:
            break
    if len(string_good) == 0 and m == 1 and e == 1 and o == 1 and w == 1:
        print("YES")
    else:
        print("NO")
    i += 1