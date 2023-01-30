N = int(input())  
A = [0] * N
B = [0] * N
for k in range(N):
    A[k] = int(input())
for k in range(N):
    B[k] = A[k]
print (A, B)