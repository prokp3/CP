def kp(n):
    for _ in range(n):
        a, b = map(int, input().split())
        ans = 1
        i = 0
        while i != b+1:
            ans = ans* i
            i += 1
        print(ans/100000007)    

n = int(input())
kp(n)        

