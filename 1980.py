def factorial(num):
    if num == 0 or num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 6
    elif num == 4:
        return 24
    elif num == 5:
        return 120
    elif num == 6:
        return 720
    elif num == 7:
        return 5040
    elif num == 8:
        return 40320
    elif num == 9:
        return 362880
    elif num == 10:
        return 3628800
    elif num == 11:
        return 39916800
    elif num == 12:
        return 479001600
    elif num == 13:
        return 6227020800
    elif num == 14:
        return 87178291200
    elif num == 15:
        return 1307674368000

s = input()
while s != "0":
    length = len(s)
    z = factorial(length)
    print(z)
    try:
        s = input()
    except EOFError:
        break