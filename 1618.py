n = int(input())
while n != 0:
    n -= 1
    ax, ay, bx, by, cx, cy, dx, dy, rx, ry = map(int, input().split())
    if rx >= ax and rx <= bx and rx >= dx and rx <= cx and ry >= ay and ry >= by and ry <= dy and ry <= cy:
        print(1)
    else:
        print(0)