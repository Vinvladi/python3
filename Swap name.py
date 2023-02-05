# example : ego.s 2.1.1.py (пробел между именем и этапом курса)
name = "GenPython"
symbol = " "  # символ между name и stage
stage = "4.1"
start = 6
end = 12
for i in range(start, end+1):
    with open(f'{name}{symbol}{stage}.{i}.py', 'w'):
        pass
