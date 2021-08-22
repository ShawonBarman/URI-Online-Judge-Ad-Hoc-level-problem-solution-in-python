while True:
    try:
        n = int(input())
        numbers = list(map(int, input().split()))[:n]
        s = sum(numbers)
        if s % n != 0:
            print(-1)
        else:
            s = int(s / n)
            ans = 0
            for i in range(n):
                if numbers[i] > s:
                    ans += numbers[i] - s
            print(ans+1)
    except EOFError:
        break