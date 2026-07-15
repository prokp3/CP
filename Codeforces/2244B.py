def kp(t):
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        k = ((n)*(n+1))//2

        possible = True

        total_books = sum(arr)
        sum_before = 0

        for i in range(n):
            sum_before += arr[i]

            req = (i+1)*(i+2)//2

            if sum_before < req:
                possible = False
                break

        if possible == True:
            print("YES")
        else:
            print("NO")        
            
           

t = int(input())
kp(t)

