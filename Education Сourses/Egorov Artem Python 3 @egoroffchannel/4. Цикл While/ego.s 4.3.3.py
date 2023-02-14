number = 1234567890
count = 0
while number > 0:
    last_digit = number % 10
    if last_digit < 3:
        count = count + 1
    number = number // 10
print(count)