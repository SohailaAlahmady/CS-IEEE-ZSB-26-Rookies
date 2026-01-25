n = int(input())
weights = list(map(int, input().split()))

total = sum(weights)
ans = float('inf')

def dfs(i, current_sum):
    global ans
    if i == n:
        diff = abs(total - 2 * current_sum)
        ans = min(ans, diff)
        return
    
    dfs(i + 1, current_sum + weights[i])

    dfs(i + 1, current_sum)

dfs(0, 0)
print(ans)