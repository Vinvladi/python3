forma_komnat = input()

if forma_komnat == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a+b+c)/2
    S = (p*(p-a)*(p-b)*(p-c))**0.5
elif forma_komnat == "прямоугольник":
    a =int(input())
    b =int(input())
    S = a*b
elif forma_komnat == "круг":
    r = int(input())
    pi = 3.14
    S = pi * (r**2)
print(S)
