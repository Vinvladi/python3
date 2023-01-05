import math

a,b,c = map(int,input().split()) # c - высота (a, b - длина и ширина)
print(math.ceil((2*a*c+2*b*c)/16))