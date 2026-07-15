def position(n):
    for i in range(n):
        
        a, b, c, d = map(int, input().split())

        total = 0
        if a < b:
            total += 1
        if a < c:
            total += 1
        if a < d:
            total += 1

        print(total)        


n = int(input())
position(n)
