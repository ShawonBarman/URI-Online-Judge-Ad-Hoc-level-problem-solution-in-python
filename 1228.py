while True:
    try:
        n = int(input())
        starting = list(map(int, input().split()))[:n]
        ending = list(map(int, input().split()))[:n]
        cmp = [0] * n

        for i in range(n):
            for j in range(n):
                if starting[i] == ending[j]:
                    cmp[j] = i + 25

        temp = 0
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if cmp[i] > cmp[j]:
                    temp = cmp[j]
                    cmp[j] = cmp[i]
                    cmp[i] = temp
                    count += 1
        print(count)
    except EOFError:
        break