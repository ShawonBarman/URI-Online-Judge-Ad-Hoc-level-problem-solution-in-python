while True:
    n = int(input())
    if n == 0:
        break
    arr = list(map(int, input().split()))[:n]
    k = int(input())
    while (arr[k-1] != k):
        k = arr[k-1]
    print(k)