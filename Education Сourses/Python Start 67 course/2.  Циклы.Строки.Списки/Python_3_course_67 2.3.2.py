a = int(input())
b = int(input())
sum_a = 0
count = 0
for i in range(a,b+1,1):
    if i%3 == 0:
        sum_a += i
        count += 1
if count == 0:
    print("No work")
else:
    print(sum_a/count)