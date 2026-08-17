def kp(t):
    for _ in range(t):
        n = int(input())
        s = list(input())

        count = 1
        max_count = 1

        for i in range(n-1):
            if s[i] == s[i+1]:
                count += 1
                max_count = max(count, max_count)

            else:
                count = 1

        print(max_count + 1)

t = int(input())
kp(t)