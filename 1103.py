while True:

    try:

        h1, m1, h2, m2 = map(int, input().split())

        if h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0:
            break

        hour = 0
        minute = 0

        if h2 > h1:
            hour = h2 - h1
            if m2 > m1:
                minute = m2 - m1
            elif m1 > m2:
                minute = (60 + m2) - m1
                hour -= 1
            else:
                minute = 0
        elif h1 > h2:
            hour = (24 + h2) - h1
            if m2 > m1:
                minute = m2 - m1
            elif m1 > m2:
                minute = (60 + m2) - m1
                hour -= 1
            else:
                minute = 0
        else:
            if m2 > m1:
                hour = 0
                minute = m2 - m1
            elif m1 > m2:
                hour = 23
                minute = (60 + m2) - m1
            else:
                hour = 0
                minute = 0

        print((hour * 60) + minute)

    except EOFError:
        break