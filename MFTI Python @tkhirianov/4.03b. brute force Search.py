def is_simple_number (k):
    divisor = 2
    while divisor < k:
        if k%divisor == 0:
            return False
        divisor +=1
    return True

k,n = map(int,input().split())
for k in range(k,n+1,1):
    if is_simple_number (k) == True:
        print (k)
