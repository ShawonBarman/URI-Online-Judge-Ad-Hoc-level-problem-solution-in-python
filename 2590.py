t = int(input())
digits = [1, 7, 9, 3]
while t != 0:
    t -= 1
    n = int(input())
    n %= 4
    print(digits[n])