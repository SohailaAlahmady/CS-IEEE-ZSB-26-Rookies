n = int(input())
str = input().strip()

let = set()

for ch in str:
    let.add(ch.lower())

if len(let) == 26:
    print("YES")
else:
    print("NO")