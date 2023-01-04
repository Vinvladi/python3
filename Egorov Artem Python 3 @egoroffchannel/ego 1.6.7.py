x,y,z = map(int,input().split())
a = 3 # стоимость карандаша
price = x*3 + y*(a+2) + z*(a+2+7)
print(price)