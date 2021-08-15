while True:
    try:

        x, y = input().split()
        print(int(x) ^ int(y))

    except EOFError:
        break