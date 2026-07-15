def kp(x1, x2, x3):
    middle = (x2-x1) + (x3-x2)
    print(middle)

x1, x2, x3 = sorted(map(int, input().split()))
kp(x1, x2, x3)