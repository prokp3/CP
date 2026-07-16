def kp(t):
    for _ in range(t):
        n = int(input())
        s = input()
        
        if "..." in s:
              print(2)
        else:
             print(s.count("."))      

t = int(input())
kp(t)                 


#Basically infinite water source ban jaata hai