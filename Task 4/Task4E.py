from itertools import permutations

s = input().strip()

perms = sorted(set(permutations(s)))

print(len(perms))
for p in perms:
    print(''.join(p))