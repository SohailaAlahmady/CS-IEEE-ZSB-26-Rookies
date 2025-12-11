n = int(input())

for _ in range(n):
    l = int(input())
    str = input()

    seen = []
    balloons = 0

    for ch in str:
        if ch in seen:
            balloons += 1
        else:
            balloons += 2
            seen.append(ch)

    print(balloons)