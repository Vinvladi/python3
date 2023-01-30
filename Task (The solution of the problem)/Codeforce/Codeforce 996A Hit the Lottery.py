n = int(input())
k = n//100 + n%100//20 + n%100%20//10 + n%10//5 + n%10%5
print(k)