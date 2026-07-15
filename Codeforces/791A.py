def weight(a, b):
    t = 0
    while a <= b:
        t +=1
        a = a*3
        b = b*2
    print(t)    



s = input().split()
a = int(s[0])
b = int(s[1])

weight(a, b)