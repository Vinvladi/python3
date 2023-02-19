# example : ego.s 2.1.Leetcode 1. Two Sum .py (пробел между именем и этапом курса)
name_list = ["ego.s", "mail.deluxe"]
name = name_list[1]
symbol = " "  # символ между name и stage
stage = "1.4"
start = 12
end = 14
for i in range(start, end+1):
    with open(f'{name}{symbol}{stage}.{i}.py', 'w'):
        pass
