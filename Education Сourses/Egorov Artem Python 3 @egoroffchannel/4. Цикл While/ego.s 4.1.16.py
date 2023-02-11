i = int(input())
a = str(i)
while a[0] != "1" and i < 1_000_000_000:  # одно из условий, что число не может быть больше 1 миллиарда
    i = int(a) * int(a[0])
    a = str(i)
print(int(a))
