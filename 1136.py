while True:
    n, b = map(int, input().split())

    if n == 0 and b == 0:
        break

    count = n+1
    b_list = list(map(int, input().split()))[:b]
    arr = [0] * (n+1)

    for i in range(b):
        arr[b_list[i]] = True
        count -= 1

    for i in range(b-1):
        for j in range(i+1, b):
            anx = abs(b_list[i] - b_list[j])
            if arr[anx] == False:
                arr[anx] = True
                count -= 1

    if count != 0:
        print("N")
    else:
        print("Y")