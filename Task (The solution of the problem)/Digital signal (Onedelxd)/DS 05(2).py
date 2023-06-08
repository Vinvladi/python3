import math

for i in range(0, 9, 1):
    print(f"Для {i}*pi/4")
    d = (1 + 1.4 * math.cos(i) + 1.6 * (math.cos(i)) ** 2) ** 2 + (1.4 * math.sin(i) + 1.6 * (math.sin(i)) ** 2) ** 2
    a = 0.16 * (8 * math.sin(i) + 7) * (math.sin(i)) ** 2 + 0.2 * (4 * math.cos(i) + 3) * (
                1.6 * (math.cos(i)) ** 2 + 1.4 * math.cos(i) + 1)
    a_i = 0.04 * (32 * math.sqrt(2) * math.sin(i) * math.sin(i + (math.pi / 4)) + 24 * math.sin(i) - 31) * math.sin(i)
    good = math.sqrt((a / d) ** 2 + (a_i / d) ** 2)
    print(good)
    im = (a_i / d) ** 2
    re = (a / d) ** 2
    good_arc = math.atan(im / re)
    print(f"Im = {im}, Re = {re} , arc.tg = {good_arc}")
