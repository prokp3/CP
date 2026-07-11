def mn(x, m):

    m += 1
    if m in x:
        mn(x, m)
    else:
        print(m)    

m = 0
n = input()
x = list(map(int, input().split()))
mn(x, m)