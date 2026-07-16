def kp(t):
    for _ in range(t):
        n, x = map(int, input().split())

        arr = list(map(int, input().split()))

        big_diff = 0
        diff = 0
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff > big_diff:
                big_diff = diff

        start_diff = arr[0]
        if start_diff > big_diff:
            big_diff = start_diff

        end_diff = 2*(x - arr[n-1])
        if end_diff > big_diff:
            big_diff = end_diff
        print(big_diff)

t = int(input())
kp(t)                        