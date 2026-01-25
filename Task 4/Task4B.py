def collatz(n):
    print(n, end=' ')
    if n == 1:
        return
    if n % 2 == 0:
        collatz(n // 2)
    else:
        collatz(3 * n + 1)

n = int(input())

collatz(n)