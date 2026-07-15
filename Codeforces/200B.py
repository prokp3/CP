def orange(n, p):
    total = sum(map(int, p.split()))
    print(total/n)


    
n = int(input())
p = input()    

orange(n, p)