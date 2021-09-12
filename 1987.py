while True:
    try:
        n, m = input().split()
        sum = 0
        for x in m:
            sum += int(x)
        if sum % 3 == 0:
            print(f"{sum} sim")
        else:
            print(f"{sum} nao")
    except EOFError:
        break