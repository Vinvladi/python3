natural = list(map(int, input().split()))
n1 = natural[:3]
n2 = natural[3:]
n1.sort()
n2.sort()
print(n1[0]*n2[0] + n1[1]*n2[1] + n1[2]*n2[2])

