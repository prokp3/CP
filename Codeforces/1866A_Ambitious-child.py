def kp(n):
    arr = list(map(int, input().split()))

    for i in range(n):
        
        arr[i] = abs(arr[i])
    smallest = min(arr)
    print(smallest)

n = int(input())
kp(n)    
