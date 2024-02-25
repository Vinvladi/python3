# example : ego.s 2.1.Leetcode 1. Two Sum .py (пробел между именем и этапом курса), EM.Python 02.01
name_list = ["ego.s", "mail.deluxe", "EM.Python", "Python_3_course_67", "GenPython"]
name = name_list[4]
symbol = " "  # символ между name и stage
stage = "4.2"
start = 9
end = 16
for i in range(start, end+1):
    with open(f'{name}{symbol}{stage}.{i}.py', 'w'):
        pass
