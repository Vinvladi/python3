# example : ego.s 2.1.Leetcode 1. Two Sum .py (пробел между именем и этапом курса), EM.Python 02.01
name_list = ["ego.s", "mail.deluxe", "EM.Python"]
name = name_list[0]
symbol = " "  # символ между name и stage
stage = "5.9"
start = 3
end = 11
for i in range(start, end+1):
    with open(f'{name}{symbol}{stage}.{i}.py', 'w'):
        pass
