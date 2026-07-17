def kp(t):
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))

        if s[0] == 1:
            print("YES")
        else:
            print("NO")

t = int(input())
kp(t)            