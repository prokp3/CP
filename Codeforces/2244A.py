def kp(t):
    for _ in range(t):
        n = int(input())
        s = input()
        

        max_count = 0
        cont = 0

        for i in range(n):
            if s[i] == "#":
                cont += 1
                if max_count<cont:
                    max_count = cont
            else:
                cont = 0     
        ans = (max_count+1)//2

        print(ans)           
                

          
        


t = int(input())
kp(t)                            