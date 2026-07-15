def kp(t):
    for _ in range(t):
        s = input()
        if s == "abc" or s == "acb" or s == "cba" or s == "bac":
            print("YES")
        else:
            print("NO")    

t = int(input())            
kp(t)