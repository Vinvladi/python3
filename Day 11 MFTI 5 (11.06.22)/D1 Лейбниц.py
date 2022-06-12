# Ряд Лейбница двумя различными способами через модуль и без него.
s = 0.0
for i in range(1, 21, 2): 
    s = 4.0 / i - s
    print (s)
print(abs(s))

a = 0
for i in range(10): 
    a += 4/(2*i+1)*(-1)**i
    print(a)
print(a)