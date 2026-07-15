def kp(n):
    for i in range(1, n+1):
        if i == 1:
            ans = 0
        elif i == 2:
            ans = 6
        else:
            ans = ((i**2)*((i**2)-1)//2) - 4*((i-2)*(i-1)) 

        print(ans)

n = int(input())     
kp(n)          