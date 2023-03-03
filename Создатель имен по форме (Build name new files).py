# example : ego.s 2.1.Leetcode 1. Two Sum .py (пробел между именем и этапом курса), EM.Python 02.01
name_list = ["ego.s", "mail.deluxe", "EM.Python"]
name = name_list[2]
symbol = " "  # символ между name и stage
stage = "ex.2"
start = 4
end = 7
for i in range(start, end+1):
    with open(f'{name}{symbol}{stage}.{i}.py', 'w'):
        pass
