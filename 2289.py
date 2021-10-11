while True:

    x, y = input().split()

    x = int(x)

    y = int(y)

    if x == 0 and y == 0:
        break

    ans = 0

    z = x ^ y
    
    while z > 0:

        ans += (z & 1)

        z >>= 1

    print(ans)
