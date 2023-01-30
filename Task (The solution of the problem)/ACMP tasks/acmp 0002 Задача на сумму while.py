i = int(input())
y,c = 1,0
if i>0:
    while y<=i :
        c = c+y
        y += 1 #x := x+1
else:
   while y>=i:
       c = c+y
       y -= 1
print (int(c))
