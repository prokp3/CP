def kp(t):

    for _ in range(t):
        a, b, c = sorted(map(int, input().split()))
        if a == b or a == c or b == c:
            print(0)
            break
        else:
            high = max(a, b, c)
            low = min(a, b, c)
        
            count = 0
            while high > low:
                high -= 1
                low += 1
                count += 1

                high = max(a, b, c)
                low = min(a, b, c)

        

            print(count)

t = int(input())
kp(t)
