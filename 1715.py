while True:
    try:
        n, m = map(int, input().split())
        count = 0
        for i in range(n):
            x = list(map(int, input().split()))[:m]
            if x.count(0) == 0:
                count += 1
        print(count)
    except EOFError:
        break