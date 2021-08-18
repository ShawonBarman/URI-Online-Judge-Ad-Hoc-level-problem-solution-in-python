while True:
    b, n = map(int, input().split())
    if b == 0 and n == 0:
        break
    r = list(map(int, input().split()))[:b]
    for i in range(n):
        d, c, v = map(int, input().split())
        r[d-1] -= v
        r[c-1] += v
    flag = "S"
    for i in r:
        if i < 0:
            flag = "N"
            break
    print(flag)