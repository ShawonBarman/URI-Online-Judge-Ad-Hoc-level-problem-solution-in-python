while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        a, b, c, d, e = map(int, input().split())
        ans = ""

        if a <= 127:
            ans += "A"
        if b <= 127:
            ans += "B"
        if c <= 127:
            ans += "C"
        if d <= 127:
            ans += "D"
        if e <= 127:
            ans += "E"

        if len(ans) == 1:
            print(ans)
        else:
            print("*")