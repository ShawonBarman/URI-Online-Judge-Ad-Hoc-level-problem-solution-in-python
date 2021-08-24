while True:
    try:
        n, m = input().split()
        arr = []
        for i in range(int(n), int(m)+1):
            arr.append(i)
        count = 0
        for x in arr:
            ans = list(str(x))
            if len(ans) == len(set(ans)):
                count += 1
        print(count)
    except EOFError:
        break