# Solution:
import sys
args = sys.argv[1:]
if args:
    numbers = ''.join(args)
    total = 0
    for num in numbers:
        total += int(num)
    print(total)