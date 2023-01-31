import sys
for line in sys.stdin:
    numbers = [int(x) for x in line.strip().split()]
    print(numbers)