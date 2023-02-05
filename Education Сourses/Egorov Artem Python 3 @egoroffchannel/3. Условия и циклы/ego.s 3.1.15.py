i = int(input())
if (i//100000+i//10000%10 + i//1000%10) == (i//100%10 + i//10%10 + i%10):
    print("YES")
else:
    print("NO")