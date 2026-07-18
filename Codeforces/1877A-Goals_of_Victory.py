def kp(t):
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        total = sum(a)
        eff = -(total)
        print(eff)

t = int(input())
kp(t)        