while True:
    n = int(input())
    if n == 0:
        break
    win_A = 0
    win_B = 0
    while n != 0:
        n -= 1
        a, b = input().split()
        if int(a) > int(b):
            win_A += 1
        elif int(a) < int(b):
            win_B += 1
    print(win_A, win_B)