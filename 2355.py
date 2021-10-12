import math
while True:
    n = int(input())
    if n == 0:
        break
    print(f"Brasil {math.floor(n/90)} x Alemanha {math.ceil(7*(n/90))}")