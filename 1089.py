while True:
    n = int(input())
    if n == 0:
        break
    h = list(map(int, input().split()))[:n]
    h.append(h[0])
    h.append(h[1])
    # print(h)
    count = 0
    i = 1
    while i != len(h)-1:
        if h[i] < h[i-1] and h[i] < h[i+1]:
            count += 1
        elif h[i] > h[i-1] and h[i] > h[i+1]:
            count += 1
        i += 1
    print(count)