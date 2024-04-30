i = str(input()) # format = 2019_03_16 15_14_00
year = i[0:4]
mount = i[5:7]
day = i[8:10]
time_hour = i[11:13]
time_minute = i[14:16]
time_sec = i[17:19]
print(f'{year}-{mount}-{day}')
print(f'{time_hour}:{time_minute}:{time_sec}')

print(f'[{year}-{mount}-{day}, {time_hour}:{time_minute}:{time_sec}],')
"""

"""
