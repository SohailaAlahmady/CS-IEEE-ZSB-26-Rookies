n, k = map(int, input().split())
r = list(map(int, input().split()))
y = r[:]

for i in range(1, 2*n, 2):
    if k == 0:
            break
    if y[i] - 1 > y[i-1] and y[i] - 1 > y[i+1]:
        y[i] -= 1
        k -= 1

print(*y)