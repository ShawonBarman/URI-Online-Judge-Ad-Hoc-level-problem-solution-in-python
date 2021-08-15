def func(n, count):
    result = 0
    for i in range(1, n):
        result += count
        result %= i
    return result

while True:
    n = int(input())
    if n == 0:
        break
    count = 1
    while True:
        if func(n, count) != 11:
            count += 1
        else:
            break
    print(count)