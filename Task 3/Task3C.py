X, Y = map(float, input().split())
bank = 0.50

if X % 5 == 0 and (X + bank) <= Y:
    Y -= (X + bank)
print(f"{Y:.2f}")