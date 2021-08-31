n = int(input())
while n != 0:
    n -= 1
    a, x, b = input().split()
    B, X, A = input().split()
    a = int(a)
    b = int(b)
    A = int(A)
    B = int(B)
    if a+A > b+B:
        print("Time 1")
    elif a+A < b+B:
        print("Time 2")
    else:
        if A > b:
            print("Time 1")
        elif A < b:
            print("Time 2")
        else:
            print("Penaltis")