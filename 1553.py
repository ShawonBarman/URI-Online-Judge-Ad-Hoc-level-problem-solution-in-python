while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    numbers = list(map(int, input().split()))[:n]
    arr = list()
    count = 0
    for num in numbers:
        if numbers.count(num) >= k and num not in arr:
            count += 1
            arr.append(num)
    print(count)