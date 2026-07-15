def spiral(t):
    for i in range(t):
        y, x = map(int, input().split())
        k = max(x, y)
        
        if k % 2 == 0:
            if x == k:
                z = (k - 1) ** 2 + y
            else:
                 z = k ** 2 - x + 1
        else:
            if y == k:
                z = (k - 1) ** 2 + x
            else:
                z = k ** 2 - y + 1
        print(z)

t = int(input())
spiral(t)                
