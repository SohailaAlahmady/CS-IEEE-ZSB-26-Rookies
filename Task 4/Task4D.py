s1 = input().strip()
s2 = input().strip()

target = 0
for c in s1:
    target += 1 if c == '+' else -1

correct = 0
total = 0

def dfs(i, pos):
    global correct, total
    if i == len(s2):
        total += 1
        if pos == target:
            correct += 1
        return

    if s2[i] == '+':
        dfs(i + 1, pos + 1)
    elif s2[i] == '-':
        dfs(i + 1, pos - 1)
    else:  # '?'
        dfs(i + 1, pos + 1)
        dfs(i + 1, pos - 1)

dfs(0, 0)
print(correct / total)