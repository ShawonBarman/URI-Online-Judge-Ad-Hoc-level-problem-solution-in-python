while True:
    try:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        l = int(input())
        k = int(input())
        x = list(map(int, input().split()))[:k]

    except EOFError:
        break

#solution will come in future.