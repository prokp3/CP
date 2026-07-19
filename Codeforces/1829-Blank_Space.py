def kp(t):
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        count = 0
        streak = 0

        for x in a:
            if x == 0:
                count +=1
                streak = max(count, streak)
            else:
                count = 0    
        
        print(streak) 

t = int(input())
kp(t)                  
