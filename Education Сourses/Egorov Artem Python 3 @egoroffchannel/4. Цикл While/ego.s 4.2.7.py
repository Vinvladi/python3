n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a + b
result = []
i = 0
d = 0
while i < n + m:
    d = min(c)
    c.remove(d)
    result.append(d)
    i += 1
print(*result)
