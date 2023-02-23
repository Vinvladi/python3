a = [[0, 2, 4, 6],
     [1, 5, 9, 13],
     [3, 10, 17, 19]
     ]
for i in a:
    print(i)

for i in a:
    for j in i:
         j += 10
         print(j, end=' ')
    print()

print(a)