time = int(input())

h = time//60//60%24
m1 = time//60%60//10
m2 = time//60%60%10
sec1 = time%60//10
sec2 = time%60%10
print(h,":",m1,m2,":",sec1,sec2, sep="")