while True:
    a, b = input().split()
    if a == '0' and b == '0':
        break
    print((2 * int(a)) - int(b))