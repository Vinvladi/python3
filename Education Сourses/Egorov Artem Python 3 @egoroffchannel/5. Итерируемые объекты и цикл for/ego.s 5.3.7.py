znak = input()
str_good = list(map(str,input().split()))
for i in str_good:
    if znak.lower() in i or znak.upper() in i:
        print(i)