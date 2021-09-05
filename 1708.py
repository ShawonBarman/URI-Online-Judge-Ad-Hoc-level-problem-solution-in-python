import math
while True:
    try:
        x, y = map(int, input().split())
        x = y - x
        ans = math.ceil(y/x)
        print(ans)
    except EOFError:
        break