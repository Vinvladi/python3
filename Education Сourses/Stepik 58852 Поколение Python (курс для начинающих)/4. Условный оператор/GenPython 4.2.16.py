i_1 = int(input())
j_1 = int(input())
i_2 = int(input())
j_2 = int(input())
if 0 < i_1 < 9 and 0 < j_1 < 9 and 0 < i_2 < 9 and 0 < j_2 < 9:
    if ((i_1 == i_2) or (i_1 + 1 == i_2) or (i_1 - 1 == i_2)) and ((j_1 == j_2) or (j_1 + 1 == j_2) or (j_1 - 1 == j_2)):
        print("YES")
    else:
        print("NO")
else:
    print("NO")