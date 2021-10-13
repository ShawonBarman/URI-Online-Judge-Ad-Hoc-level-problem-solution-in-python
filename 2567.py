while True:
    try:
        n = int(input())
        ai = list(map(int, input().split()))[:n]
        ai.sort()
        j = n - 1
        total, i = 0, 0
        while j > i:
            total += abs(ai[i] - ai[j])
            j -= 1
            i += 1
        print(total)
    except EOFError:
        break