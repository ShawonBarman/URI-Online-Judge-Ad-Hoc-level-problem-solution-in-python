while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    ans = (a*b*c)**(1/3)
    print(int(ans))