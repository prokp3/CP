def kp(t):
    for _ in range(t):
        n = int(input())
        
        
        if (n % 2 != 0) or n < 4:
            print(-1)
        elif n == 4:
            min_bus = 1
            max_bus = 1
            print(min_bus, max_bus)
        else:
            n2 = n//2
            max_bus = (n2//2)
            min_bus = ((n2+2)//3)
            print(min_bus, max_bus)

t = int(input())
kp(t)

            

