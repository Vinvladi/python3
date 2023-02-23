count = 0
for n1 in range(1,10,1):
    for n2 in range(0, 10, 1):
        for n3 in range(0, 10, 1):
            for n4 in range(0, 10, 1):
                if n1 + n2 + n3 + n4 == 20:
                    good_number = 1000*n1 + 100*n2 + 10*n3 + n4
                    count += good_number
print(count)