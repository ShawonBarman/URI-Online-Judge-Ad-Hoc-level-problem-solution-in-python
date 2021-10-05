def funct(a, b):
    tmp = a % b
    while tmp != 0:
        a = b
        b = tmp
        tmp = a % b
    return b
a, b, c, d = map(int, input().split())
x = a * d + b * c
y = b * d
temp = funct(x, y)
print(f"{int(x/temp)} {int(y/temp)}")