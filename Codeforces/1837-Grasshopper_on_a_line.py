def kp(t):
    for _ in range(t):
        
        x, k = map(int, input().split())
        if x % k == 0:
            print(2)
            print(1, x-1)
        else:
            print(1)
            print(x)

t = int(input())
kp(t)