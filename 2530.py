while True:
    try:
        n, m = map(int, input().split())
        juan_ans = list(map(int, input().split()))[:n]
        ricardinho_ans = list(map(int, input().split()))[:m]
        i = j = 0
        while i < m and j < n:
            if ricardinho_ans[i] == juan_ans[j]:
                i += 1
            j += 1
        if i == m:
            print("sim")
        else:
            print("nao")
    except EOFError:
        break