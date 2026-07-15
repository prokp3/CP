def kp(t):
    for _ in range(t):
        n = int(input())
        arr = []
        i = 1

        while i+1 <=n:
            arr.append(i+1)
            arr.append(i)
            i+=2

        if i == n:
            arr.append(i)    
        print(*arr)


t = int(input())
kp(t)            