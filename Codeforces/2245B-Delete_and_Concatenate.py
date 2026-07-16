def kp(t):
    for _ in range(t):
        n, c = map(int, input().split())
        arr = list(map(int, input().split()))
        single_Benifit = sum(arr) - n*c

        for i in range(1, n-1):
            if min(arr[i-1], arr[i]) < c or min(arr[i], arr[i+1]) < c:
                benifit1 = max(arr[i-1], arr[i]) - c
                benifit2 = max(arr[i], arr[i+1]) - c
                double_benifit = max(benifit1, benifit2)
                   
