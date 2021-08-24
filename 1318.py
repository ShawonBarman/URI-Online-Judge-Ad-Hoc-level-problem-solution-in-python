while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    t = list(map(int, input().split()))[:m]
    count = 0
    arr = []
    for x in t:
        if t.count(x) > 1:
            if x not in arr:
                arr.append(x)
                count += 1
    print(count)