a,b,c = map(int,input().split())
print("YES" if a + b == c or a + c == b or b + c == a else "NO")