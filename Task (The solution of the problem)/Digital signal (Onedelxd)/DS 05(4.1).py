import math
for i in range(0, 9, 1):
    print(f"Для {i}*pi/4")
    d = (1 + 1.4 * math.cos(i*math.pi/4) + 1.6 * (math.cos(i*math.pi/4))**2)**2 + (1.4 * math.sin(i*math.pi/4) + 1.6 * (math.sin(i*math.pi/4))**2)**2
    a = -0.96 * math.sin(i*math.pi/4)**2 + 0.96 * math.cos(i*math.pi/4)**2 + 2.92 * math.cos(i*math.pi/4) + 1.72
    a_i = math.sin(i*math.pi/4) * (1.92 * math.cos(i*math.pi/4) + 1.32)
    good = math.sqrt((a/d)**2+(a_i/d)**2)
    print(good)
    im = (a_i/d)**2
    re = (a/d) ** 2
    good_arc = math.atan(im/re)
    print(f"Im = {im}, Re = {re} , arc.tg = {good_arc}")
