print(int(input()) + int(input()))  # 1-ый вариант
print(sum((int(input()) for i in range(2)))) # 2-ой вариант
a, b = input().split()  # 3-ий вариант
print(int(a) + int(b))