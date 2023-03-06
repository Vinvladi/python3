lst = list(map(int, input().split()))
i = int(input())
count = 0
for number, item in enumerate(lst):
    if i == item:
        print(number, end=" ")
        count += 1
if count == 0:
    print("Отсутствует")
