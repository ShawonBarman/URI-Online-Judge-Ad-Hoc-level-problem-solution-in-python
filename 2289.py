def converter(n):
    ans = bin(n).replace("0b", "")
    print(ans)
    return ans

while True:
    x, y = map(int, input().split())
    if x == y == 0:
        break
    x = converter(x)
    y = converter(y)
    if len(x) > len(y):
        while len(y) != len(x):
            y = '0' + y
    elif len(y) > len(x):
        while len(x) != len(y):
            x = '0' + x
    count = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            continue
        else:
            count += 1
    print(count)