while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    caracterists = 4
    programmer = []
    for i in range(n):
        arr = list(map(int, input().split()))[:m]
        programmer.append(arr)

    #condition 1
    for i in range(n):
        p = programmer[i].count(1)
        if p == m:
            caracterists -= 1
            break
    # condition 2
    test = [0]*m
    for i in range(n):
        for j in range(m):
            if programmer[i][j] == 1:
                test[j] += 1
    if test.count(0) > 0:
        caracterists -= 1
    # condition 3
    for i in range(m):
        if test[i] == n:
            caracterists -= 1
            break
    # condition 4
    for i in range(n):
        p = programmer[i].count(0)
        if p == m:
            caracterists -= 1
            break

    print(caracterists)