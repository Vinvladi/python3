name = "ego.s"
stage = "2.8"
start = 3
end = 4
for i in range(start, end+1):
    with open(f'{name} {stage}.{i}.py', 'w'):
        pass
