# example : ego.s 2.1.1.py (пробел между именем и этапом курса)
name_list = ["ego.s", "mail"]
name = "ego.s"
symbol = " "  # символ между name и stage
stage = "4.2"
start = 2
end = 8
for i in range(start, end+1):
    with open(f'{name}{symbol}{stage}.{i}.py', 'w'):
        pass
