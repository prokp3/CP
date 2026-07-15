def mn(n, x):
    real_sum = (n*(n+1))//2
    total = sum(x)
    number = real_sum - total
    print(number)

n = int(input())
x= list(map(int, input().split()))
mn(n, x)