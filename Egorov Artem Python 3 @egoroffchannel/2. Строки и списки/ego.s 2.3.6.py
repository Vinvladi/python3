i = str(input()) # мне не нравиться мое решение из-за того, что оно большое
i1 = i[0:3]
i2 = i[-3:]
i3 = i[3:-3]
i1 = i1.upper()
i2 = i2.upper()
i3 = i3.lower()
f1 = i1 + i3 + i2
print(f1)
