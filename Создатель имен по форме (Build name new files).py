# example : ego.s 2.1.Leetcode 1. Two Sum .py (пробел между именем и этапом курса)
name_list = ["ego.s", "mail.deluxe"]
name = name_list[0]
symbol = " "  # символ между name и stage
stage = "5.2"
start = 2
end = 15
for i in range(start, end+1):
    with open(f'{name}{symbol}{stage}.{i}.py', 'w'):
        pass
