def kp(t):
    for _ in range(t):
        n, p = map(int, input().split())
        rem_people = n
        share_lim = list(map(int, input().split()))
        share_price = list(map(int, input().split()))
        pairs = sorted(zip(share_price, share_lim))
        cost = p
        rem_people -= 1

        
        for bi, ai in pairs:
        
            while ai != 0:
                if rem_people == 0:
                    break
                elif bi < p:
                    cost += bi
                    rem_people -= 1
                    ai -=1
                else:
                    cost += p*rem_people
                    rem_people = 0

        print(cost)

t = int(input())
kp(t)