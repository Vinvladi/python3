a = "Moscow"
c = [chr(ord(char) + 1) for char in a]
print('once:', *c)
print('again:', *c)
