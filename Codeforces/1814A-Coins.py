def kp(t):
    for _ in range(t):
        n, k = map(int, input().split())

        # n = 2x + ky
        if n%2 == 0 or (n-k)%2 == 0:
            print("YES")
        else:
            print("NO")    

t= int(input())
kp(t)