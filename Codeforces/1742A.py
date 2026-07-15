def sum(n):
    for i in range(n):
        d = input().split()
        a = int(d[0])
        b = int(d[1])
        c = int(d[2])

        if (a == b+c) or (b == a+c) or (c == a+b):
            print("YES")
        else:
            print("NO")


n = int(input())
sum(n)            
        