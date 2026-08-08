from math import gcd

def kp(t):
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))


        gc1 = 3

        for i in range(k):
            for j in range(k):
                gc = gcd(arr[i], arr[j])

                gc1 = min(gc, gc1)

        if gc1 <= 2:
            print("Yes")
        else:
            print("No")

                

t = int(input())
kp(t)