def num(t):
    arr = [
        [1, 2, 9, 10, 25],
        [4, 3, 8, 11, 24],
        [5, 6, 7, 12, 23],
        [16, 15, 14, 13, 22],
        [17, 18, 19, 20, 21]
    ]
    for i in range(t):
        x1, y1 = map(int, input().split())
        print(arr[x1-1][y1-1])

t = int(input())
num(t)  