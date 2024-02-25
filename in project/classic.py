filename = "all.txt"

with open(filename, "r", encoding='utf-8') as f:
    lines = f.readlines()

# Remove the newline characters from each line.
lines = [line.strip() for line in lines]


filename_1 = "d1.txt"

with open(filename_1, "r", encoding='utf-8') as f:
    lines_1 = f.readlines()

# Remove the newline characters from each line.
lines_1 = [line.strip() for line in lines_1]

for item in range(0, len(lines_1)):
    d_1 = str("Inscribed") + str(" ") + str(lines_1[item])
    lines_1.append(d_1)
    d_2 = str("Autographed") + str(" ") + str(lines_1[item])
    lines_1.append(d_2)
    d_3 = str("Corrupted") + str(" ") + str(lines_1[item])
    lines_1.append(d_3)
    d_4 = str("Auspicious") + str(" ") + str(lines_1[item])
    lines_1.append(d_4)
    d_5 = str("Genuine") + str(" ") + str(lines_1[item])
    lines_1.append(d_5)
    d_6 = str("Heroic") + str(" ") + str(lines_1[item])
    lines_1.append(d_6)
    d_7 = str("Frozen") + str(" ") + str(lines_1[item])
    lines_1.append(d_7)
    d_8 = str("Cursed") + str(" ") + str(lines_1[item])
    lines_1.append(d_8)
    d_9 = str("Infused") + str(" ") + str(lines_1[item])
    lines_1.append(d_9)
    d_10 = str("Unusual") + str(" ") + str(lines_1[item])
    lines_1.append(d_10)

for item_1 in lines:
    if item_1 in lines_1:
        continue
    else:
        print(item_1)