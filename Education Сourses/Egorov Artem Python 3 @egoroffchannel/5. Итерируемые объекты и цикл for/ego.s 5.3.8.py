numbers = map(int, input().split())
numbers_list = []
for i in numbers:
    numbers_list.append(i)
element = int(input())
count = 0
for i in range(len(numbers_list)):
    if numbers_list[i] == element:
        count = 1
        good_index = i + 1
        break
print(good_index if count == 1 else "ErrorValue")
