number = int(input())
num = number
if number > 0:
    number_list = []
    while number > 0:
        last = number % 10
        number_list.append(last)
        number = number // 10
    number_list.reverse()
    chet_number = []
    nechet_number = []
    len_number = len(number_list)
    for i in range(0,len_number):
        if i % 2 == 0:
            chet_number.append(number_list[i])
        else:
            nechet_number.append(number_list[i])
    print("YES") if (sum(nechet_number) - sum(chet_number)) % 11 == 0 else print("NO")
else:
    print("NO")
