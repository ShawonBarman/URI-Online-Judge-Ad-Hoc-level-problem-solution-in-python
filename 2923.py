while True:
    try:
        t, a, w, c = map(int, input().split())
        if (a*100)/t >= c:
            print("critical")
        elif (a*100)/t >= w:
            print("warning")
        else:
            print("OK")
    except EOFError:
        break