a = "Moscow"
b = map(lambda char: chr(ord(char) +1 ), a)
print('once:', *b)
print('again:', *b)