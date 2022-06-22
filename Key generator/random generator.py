# AE70P-6B92F-0EL6L
# random ()
import random
import openpyxl

#book =openpyxl.Workbook()
#sheet =book.active

ord('A')
ord('Z')
ord('0')
ord('9')
print(ord('A'), ord('Z'), ord('0'), ord('9'))
# 48-57 and 65-90
j, p, jp = 0, 0, 0
f = 15
d, k = str(), str()
index = 0
for index in range(f):
    j = random.randint(ord('A'), ord('Z'))
    p = random.randint(ord('0'), ord('9'))
    jp = str(chr(j))+str(chr(p))
    jp = random.choice(jp)
    k = k.join(str(jp))
    d = d + k
    if index % 5 == 4:
        k = k.join(str("-"))
        d = d + k
    index += 1
print(d[:len(d)-1])





"""sheet1 = book.active
sheet1['A1'] = 'Name'


for row in range(1, sheet.max_row):
    name = sheet[row][0].value
    sheet1[row][0].value = name
    if row == 1:
        sheet1['B1'] = 'Links'



book1.save("C:\Microsoft VS Code\Github/key generator/keys.xlsx")
book1.close() """