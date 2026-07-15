def test(n):
    for i in range(n):
        word = input()
        if word.lower() == "yes":
            print("YES")
        else:
            print("NO")    

n = int(input())
test(n)
