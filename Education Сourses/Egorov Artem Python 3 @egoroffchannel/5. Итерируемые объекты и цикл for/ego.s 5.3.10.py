good_string = input()
good_string = good_string.lower() # не забывать что надо посчитать без учета регистра
string_output = []
for i in range(len(good_string)):
    y = good_string.count(good_string[i])
    string_output.append(y)
print(max(string_output))
