while True:
    a, c = map(int, input().split())
    if a == 0 and c == 0:
        break
    x = list(map(int, input().split()))[:c]
    temp = a
    w = a
    count = 0
    flag = False
    for i in x:
        if i <= temp:
            flag = False
        else:
            if flag == False:
                count += w
                count -= temp
            w = i
            flag = True
        temp = i
    if flag == False:
        count += w
        count -= temp
    print(count)