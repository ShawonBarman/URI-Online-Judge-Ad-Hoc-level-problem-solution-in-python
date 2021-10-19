t = int(input())
while t != 0:
    t -= 1
    n, m = map(int, input().split())
    p = list(map(int, input().split()))[:n]
    count = 1
    tmp = p[0]
    for i in range(1, n):
        if tmp + p[i] > m:
            count += 1
            tmp = p[i]
        else:
            tmp += p[i]

    print(count)