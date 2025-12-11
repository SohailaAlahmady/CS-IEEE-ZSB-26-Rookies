n = int(input())

for _ in range(n):
    l = int(input())
    arr = list(map(int, input().split()))

    if(arr[0] == arr[1] or arr[0] == arr[2]):
        com = arr[0]
    else:
        com = arr[1]

    for i, val in enumerate(arr):
        if val != com:
            print(i + 1)
            break