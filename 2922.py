while True:
    try:
        b, u = map(int, input().split())
        diff = abs(b-u)-1
        if diff <= 0:
            print(0)
        else:
            print(diff)
    except EOFError:
        break