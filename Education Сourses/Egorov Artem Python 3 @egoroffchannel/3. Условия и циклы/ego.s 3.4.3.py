i = int(input())
if i % 3 != 0 and i % 5 != 0:
    print(i)
elif i%3 != 0 and i%5 == 0:
    print("Buzz")
elif i%3 == 0 and i%5 != 0:
    print("Fizz")
else:
    print("FizzBuzz")