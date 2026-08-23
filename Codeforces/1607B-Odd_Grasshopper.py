def kp(t):
    for _ in range(t):
        xo, n = map(int, input().split())
        
        

        if n % 2 == 0:
            out = -(n/2)
        else:
            out = (n//2)+1

        print(int(out) + xo)


t = int(input())
kp(t)


