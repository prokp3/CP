def rep(arr):
    streak = 1
    l_streak = 1
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            streak += 1
            if streak >= l_streak:
                l_streak = streak
        else:
            streak = 1
    print(l_streak)      

arr = list(input())
rep(arr)

      
