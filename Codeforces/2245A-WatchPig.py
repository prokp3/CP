def kp(t):
    for _ in range(t):
        n, k = map(int, input().split())
        s = list(input().strip())
        optimal = s.copy()

        if 2*k > n:
            print("-1")
        else:    
        
            for i in range(k):
                optimal[i] = "R"
            for j in range(k):
                optimal[n-j-1] = "L"
            count = 0
            for h in range(n):
                if optimal[h] != s[h]:
                    count += 1
            print(count)

t = int(input())
kp(t)                