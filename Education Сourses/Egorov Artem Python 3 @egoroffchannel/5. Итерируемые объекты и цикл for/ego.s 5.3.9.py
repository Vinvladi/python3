numbers = list(map(int, input().split()))
numbers_pozitive = []
for i in numbers:
    if i > 0:
        numbers_pozitive.append(i)
print(min(numbers_pozitive) if len(numbers_pozitive) > 0 else "Empty")
