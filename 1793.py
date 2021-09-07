while True:
    n = int(input())
    if n == 0:
        break
    t = list(map(int, input().split()))[:n]
    ans = 10
    for i in range(1, len(t)):
        ans += min(10, t[i]-t[i-1])
    print(ans)