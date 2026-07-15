def kp(arr):
    n = len(arr)
    for i in range(1, n):
        t = arr[i]
        if t > (9-t):
            t = (9-t)
            arr[i] = t
    t = arr[0]
    if t == 9:
        t = 9
        arr[0] = t
    elif t > (9-t):
        t = (9-t)
        arr[0] = t

    print(*arr, sep = "")        


arr = list(map(int, input()))
kp(arr)
             