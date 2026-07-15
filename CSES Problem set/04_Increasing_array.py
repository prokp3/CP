def ia(n, x):
    moves = 0
    for i in range(n-1):
        if x[i] >= x[i+1]:
            diff = x[i] - x[i+1]
            moves += diff
            x[i+1] = x[i]
    print(moves)

n = int(input())
x = list(map(int, input().split()))  
ia(n, x)