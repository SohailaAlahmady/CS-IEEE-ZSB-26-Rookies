N, K = map(int, input().split())
c = 0

while N > 0:
    N //= K
    c += 1
print(c)