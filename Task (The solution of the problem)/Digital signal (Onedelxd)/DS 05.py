import math
for i in range(0, 9, 1):
    print(f"Для {i}*pi/4")
    good = math.sqrt(((0.5+0.35*math.cos(i*math.pi/4))/(1.49+1.4*math.cos(i*math.pi/4)))**2+(((0.35*math.sin(i*math.pi/4))/(1.49+1.4*math.cos(i*math.pi/4)))**2))
    print(good)
    im = ((0.35*math.sin(i*math.pi/4))/(1.49+1.4*math.cos(i*math.pi/4)))**2
    re = ((0.5 + 0.35 * math.cos(i * math.pi / 4)) / (1.49 + 1.4 * math.cos(i * math.pi / 4))) ** 2
    good_arc = math.atan(im/re)
    print(f"Im = {im}, Re = {re} , arc.tg = {good_arc}")