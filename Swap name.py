# example : ego.s 2.1.1.py (пробел между именем и этапом курса)
name = "ego.s"
symbol = " "  # символ между name и stage
stage = "3.3"
start = 3
end = 9
for i in range(start, end+1):
    with open(f'{name}{symbol}{stage}.{i}.py', 'w'):
        pass
