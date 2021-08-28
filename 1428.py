import math
t = int(input())
while t != 0:
    t -= 1
    n, m = map(int, input().split())
    a = math.ceil((n-2)/3)
    b = math.ceil((m-2)/3)
    print(a*b)