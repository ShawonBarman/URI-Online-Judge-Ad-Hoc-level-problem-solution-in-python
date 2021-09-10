t = int(input())
while t:
    t -= 1
    c, d = map(int, input().split())
    if (26**c) * (10**d) == 1:
        print(0)
    else:
        print((26**c) * (10**d))