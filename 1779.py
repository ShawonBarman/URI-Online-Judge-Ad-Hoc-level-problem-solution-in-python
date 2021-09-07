t = int(input())
count = 1
while t != 0:
    t -= 1
    n = int(input())
    array = list(map(int, input().split()))[:n]
    m = max(array)
    r, k = 0, 0
    for i in range(len(array)):
        if array[i] == m:
            k += 1
        else:
            k = 0
        r = max(r, k)
    print(f"Caso #{count}: {r}")
    count += 1