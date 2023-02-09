n1,n2,o = float(input()),float(input()), input()
if o == "+":
    print(n1+n2)
elif o == "-":
    print(n1-n2)
elif o == "*":
    print(n1*n2)
elif o == "/" and n2 !=0:
    print(n1/n2)
else:
    print("Неизвестно")