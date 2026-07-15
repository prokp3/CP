def kp(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                x = i
                y = j

    ans = abs(x-2) + abs(y-2)  
    print(ans)          

arr = [list(map(int, input().split())) for _ in range(5)]
kp(arr)