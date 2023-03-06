# example : ego.s 2.1.Leetcode 1. Two Sum .py (пробел между именем и этапом курса), EM.Python 02.01
name_list = ["ego.s", "mail.deluxe", "EM.Python", "Python_3_course_67"]
name = name_list[3]
symbol = " "  # символ между name и stage
stage = "1.6"
start = 3
end = 7
for i in range(start, end+1):
    with open(f'{name}{symbol}{stage}.{i}.py', 'w'):
        pass
