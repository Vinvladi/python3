# example : ego.s 2.1.1.py (пробел между именем и этапом курса)
name_list = ["ego.s", "mail.deluxe"]
name = name_list[0]
symbol = " "  # символ между name и stage
stage = "4.3"
start = 3
end = 11
for i in range(start, end+1):
    with open(f'{name}{symbol}{stage}.{i}.py', 'w'):
        pass
