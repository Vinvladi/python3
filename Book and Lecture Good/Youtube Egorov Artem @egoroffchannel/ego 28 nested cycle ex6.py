x = int(input())
s = 0
while x>0:
    s+= x%10
    x//=10
print()

for i in range(1,100001):
    x = i
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    print(i,s)