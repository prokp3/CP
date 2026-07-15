def pm(n):
    arr = []
    if n <= 3 and n > 1:
        print("NO SOLUTION")
    else:
        for i in range(2, n+1, 2):
            arr.append(i)
        for i in range(1, n+1, 2):
            arr.append(i)
        print(*arr)       
        

n = int(input())
pm(n)