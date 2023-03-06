x_timer = int(input())  # программа будет правильно работать, если не более 24 часов
h_sleep = int(input())
m_sleep = int(input())
full_minute = h_sleep*60 + m_sleep
print((full_minute + x_timer) // 60)
print((full_minute + x_timer) % 60)