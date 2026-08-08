def kp(t):
    for _ in range(t):

        n = int(input())
        arr = [int(d) for d in input().strip()]

        while len(arr) >= 2:
            if arr[0] != arr[-1]:
                del arr[0]
                del arr[-1]
            else:
                break
        print(len(arr))
        

t = int(input())
kp(t)