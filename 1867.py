while (True):
    n, m = input().split()
    if (n == '0' and m == '0'):
        break

    while (len(n) > 1):
        n1 = 0
        for i in n:
            n1 += int(i)
        n = str(n1)

    while (len(m) > 1):
        m1 = 0
        for i in m:
            m1 += int(i)
        m = str(m1)

    if (int(n) == int(m)):
        print(0)
    elif (int(n) > int(m)):
        print(1)
    else:
        print(2)