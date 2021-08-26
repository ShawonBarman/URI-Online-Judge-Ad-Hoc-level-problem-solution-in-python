while True:
    n = int(input())
    if n == 0:
        break
    ans = 0
    for i in range(n):
        c, v = map(int, input().split())
        ans += int(v/2)
    print(int(ans/2))