def kp(t):
    for _ in range(t):
        n = int(input())

        s = list(map(int, input().split()))
        distinct = len(set(s))

        if distinct == 1:
            print("Yes")
        if distinct == 2:
            s.sort()
            count1 = 1
            
            for i in range(n-1):
                if s[i] == s[i+1]:
                    count1 +=1
                else:
                    break
            count2 = n-count1    
            if count1 == (n+1)//2 or count1 == n//2:
                if count2 == n//2 or count2 == (n+1)//2:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")    

        if distinct > 2:
            print("No")               


t = int(input())
kp(t)            