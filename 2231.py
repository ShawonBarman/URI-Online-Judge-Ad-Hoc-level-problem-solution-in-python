count = 1
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    temp = []
    tempA = [0] * (n + 1)

    for i in range(n):
        temp.append(int(input()))

    for i in range(n):
        a = tempA[i]
        b = temp[i]
        tempA[i + 1] = a + b

    maxi = -9999999
    mini = 9999999
    v = 0
    u = m
    while u <= n:
        sum = tempA[u] - tempA[v]
        if sum > maxi:
            maxi = sum
        if sum < mini:
            mini = sum

        v += 1
        u += 1

    print(f"Teste {count}")
    count += 1
    print(int(mini / m), int(maxi / m))
    print()