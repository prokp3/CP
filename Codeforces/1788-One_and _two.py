def kp(t):
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        #just put half 2 in the left and the other 1 and 2's on the right
        count = 0
        for x in arr:
            if x == 2:
                count += 1

        need = count // 2
        have = 0

        if count%2 != 0:
            print(-1)

        elif count == 0:
            print(1)    

        else:

            for i in range(n):
                if arr[i] == 2:
                    have += 1
                if have == need:
                    print(i+1)
                    break




t = int(input())
kp(t)
