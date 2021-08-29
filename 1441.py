while True:
    h = int(input())
    if h == 0:
        break
    arr = list()
    arr.append(h)
    while h != 1:
        if h%2 == 0:
            h = int((0.5)*h)
            arr.append(h)
        else:
            h = 3 * h + 1
            arr.append(h)
    # print(arr)
    print(max(arr))