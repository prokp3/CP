def wa(n):
    if n == 1:
        print(n)
        return

    if n%2 == 0:
        print(n)
        n = (n//2)
        
        wa(n)

    else:
        print(n)
        n = (n*3) + 1
        wa(n)    


n = int(input())  
wa(n)      