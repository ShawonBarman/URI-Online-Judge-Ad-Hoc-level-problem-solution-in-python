while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break
    arr = []
    ans = 'no'
    another_arr = [0] * n
    for i in range(d):
        x = list(map(int, input().split()))[:n]
        arr.append(x)
    for i in range(d):
        for j in range(n):
            if arr[i][j] == 1:
                another_arr[j] += 1
    if another_arr.count(d) > 0:
        ans = 'yes'
    print(ans)